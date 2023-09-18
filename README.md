# Model Evaluation on the HumTrans Dataset
[![PWC](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-HumTrans%20Dataset-green)](https://huggingface.co/datasets/dadinghh2/HumTrans)

This is the official repository for **HumTrans: A Novel Open-Source Dataset for Humming Melody Transcription and Beyond**.

# Introduction
We present baseline results of four SOTA vocal melody transcription models on both validation and test sets of our HumTrans dataset, including [VOCANO](https://github.com/B05901022/VOCANO/tree/main), [Sheet Sage](https://github.com/chrisdonahue/sheetsage), [MIR-ST500](https://github.com/york135/singing_transcription_ICASSP2021/tree/master), and [JDC-STP](https://github.com/keums/icassp2022-vocal-transcription), shown in the following table. For all the experiments, we directly utilized the pre-trained models provided by the authors to generate predicted transcription (midis/{VOCANO.zip,SheetSage.zip,MIR-ST500.zip,JDC-STP.zip}) and compared them with the reference MIDI files (midis/GroundTruth.zip).We can observe that although JDC-STP performed slightly better than the other models, the transcription capabilities of all the models are still far from satisfactory. Therefore, there is significant room for improvement in the domain of humming melody transcription.
