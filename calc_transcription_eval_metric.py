import os
import sys
import copy
import mir_eval
import numpy as np
import pretty_midi
# from music21 import converter, note
from tqdm import tqdm


EVAL_TOLERANCE = 0.05
OCTAVE_INVARIANT_RADIUS = 16


def trim_midi(ref_midi_data, est_midi_data):
    ref_notes = []
    for i in ref_midi_data.instruments:
        if i.is_drum:
            continue
        for n in i.notes:
            ref_notes.append(n)
    segment_start = ref_notes[0].start
    segment_end = ref_notes[-1].end

    num_dropped = 0
    for i in est_midi_data.instruments:
        if i.is_drum:
            continue
        i.notes = [
            n for n in i.notes if n.start >= segment_start and n.start <= segment_end
        ]

    return est_midi_data


def midi_to_mir_eval(midi_data, dummy_offsets = True):
    notes = []
    for i in midi_data.instruments:
        if i.is_drum:
            continue
        for n in i.notes:
            notes.append((n.start, n.end, n.pitch))
    notes = sorted(notes)
    note_onsets = [s for s, _, _ in notes]
    note_offsets = [e for _, e, _ in notes]
    if dummy_offsets and len(note_onsets) > 0:
        note_offsets = note_onsets[1:] + [note_onsets[-1] + 1]
    intervals = np.stack([note_onsets, note_offsets], axis = 1).astype(np.float64)
    pitches = np.array([p for _, _, p in notes], dtype = np.int64)
    return intervals, pitches


def extract_notes(ref_midi_file, est_midi_file):
    ref_midi_data = pretty_midi.PrettyMIDI(ref_midi_file)
    est_midi_data = pretty_midi.PrettyMIDI(est_midi_file)
    ref_midi_data = copy.deepcopy(ref_midi_data)
    est_midi_data = copy.deepcopy(est_midi_data)

    est_midi_data = trim_midi(ref_midi_data, est_midi_data)

    ref_intervals, ref_pitches = midi_to_mir_eval(ref_midi_data, dummy_offsets = False)
    est_intervals, est_pitches = midi_to_mir_eval(est_midi_data, dummy_offsets = False)

    return ref_intervals, ref_pitches, est_intervals, est_pitches


def mir_eval_onset_prf(ref_intervals, ref_pitches, est_intervals, est_pitches):
    m_to_f = lambda m: 440.0 * np.power(2, (m.astype(np.float32) - 69) / 12)
    p, r, f1, _ = mir_eval.transcription.precision_recall_f1_overlap(
            ref_intervals,
            m_to_f(ref_pitches),
            est_intervals,
            m_to_f(est_pitches),
            onset_tolerance = EVAL_TOLERANCE,
            pitch_tolerance = 1.0,
            offset_ratio = None,
        )
    return p, r, f1


def evaluate(ref_intervals, ref_pitches, est_intervals, est_pitches):
    octaves = list(range(-OCTAVE_INVARIANT_RADIUS, OCTAVE_INVARIANT_RADIUS + 1))
    ps = []
    rs = []
    f1s = []
    for o in octaves:
        p, r, f1 = mir_eval_onset_prf(
            ref_intervals,
            (o * 12) + ref_pitches,
            est_intervals,
            est_pitches
        )
        ps.append(p)
        rs.append(r)
        f1s.append(f1)

    best_octave_idx = np.argmax(f1s)
    return (
        ps[best_octave_idx],
        rs[best_octave_idx],
        f1s[best_octave_idx]
    )


if __name__ == '__main__':
    in_file_key_list = sys.argv[1]
    in_ref_midi_folder = sys.argv[2]
    in_est_midi_folder = sys.argv[3]

    result = []
    with open(in_file_key_list) as f_r:
        for line in tqdm(f_r):
            line_strip = line.strip()
            in_ref_midi_file = os.path.join(in_ref_midi_folder, line_strip) + '.mid'
            in_est_midi_file = os.path.join(in_est_midi_folder, line_strip) + '.mid'
            ref_intervals, ref_pitches, est_intervals, est_pitches = \
                extract_notes(in_ref_midi_file, in_est_midi_file)
            res = evaluate(ref_intervals, ref_pitches, est_intervals, est_pitches)
            result.append(res)

    result = np.array(result)
    print(result.mean(axis = 0))