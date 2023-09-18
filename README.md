# Model Evaluation on the HumTrans Dataset
[![PWC](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-HumTrans%20Dataset-green)](https://huggingface.co/datasets/dadinghh2/HumTrans)

This is the official repository for **HumTrans: A Novel Open-Source Dataset for Humming Melody Transcription and Beyond**.

# Introduction
We present baseline results of four SOTA vocal melody transcription models on both validation and test sets of our HumTrans dataset, including [VOCANO](https://github.com/B05901022/VOCANO/tree/main), [Sheet Sage](https://github.com/chrisdonahue/sheetsage), [MIR-ST500](https://github.com/york135/singing_transcription_ICASSP2021/tree/master), and [JDC-STP](https://github.com/keums/icassp2022-vocal-transcription), shown in the following table. For all the experiments, we directly utilized the codes provided by the authors to generate predicted transcription (midis/{VOCANO.zip,SheetSage.zip,MIR-ST500.zip,JDC-STP.zip}) and compared them with the reference MIDI files (midis/GroundTruth.zip).We can observe that although JDC-STP performed slightly better than the other models, the transcription capabilities of all the models are still far from satisfactory. Therefore, there is significant room for improvement in the domain of humming melody transcription.

<table>
  <tr>
    <td rowspan="2">Model</td>
    <td colspan="3">Valid Set</td>
    <td colspan="3">Test Set</td>
  </tr>
  <tr>
    <td>Precison</td>
    <td>Recall</td>
    <td>F1</td>
    <td>Precison</td>
    <td>Recall</td>
    <td>F1</td>
  </tr>
  <tr>
    <td>VOCANO</td>
    <td>3.270</td>
    <td>3.314</td>
    <td>3.194</td>
    <td>3.384</td>
    <td>3.329</td>
    <td>3.352</td>
  </tr> 
  <tr>
    <td>Sheet Sage</td>
    <td>2.757</td>
    <td>2.656</td>
    <td>2.702</td>
    <td>3.039</td>
    <td>2.982</td>
    <td>3.005</td>
  </tr> 
  <tr>
    <td>MIR-ST500</td>
    <td>6.258</td>
    <td>6.448</td>
    <td>6.341</td>
    <td>5.686</td>
    <td>5.853</td>
    <td>5.755</td>
  </tr> 
  <tr>
    <td>JDC-STP</td>
    <td>6.777</td>
    <td>6.785</td>
    <td>6.741</td>
    <td>5.844</td>
    <td>5.620</td>
    <td>5.667</td>
  </tr> 
</table>
