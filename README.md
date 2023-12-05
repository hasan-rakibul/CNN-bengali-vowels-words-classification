This repository contains the codebase of [Investigation of the Effect of MFCC Variation on the Convolutional Neural Network-Based Speech Classification](https://doi.org/10.1109/TENSYMP50017.2020.9230697).

**Abstract:** This paper deals with the step-by-step implementation of a Bengali speech classification model with the variations of Mel-Frequency Cepstral Coefficient (MFCC). A deep convolutional neural network is developed for the classification purpose. Bengali vowels are the representative of the lower MFCC variational group, and words are the higher variational group. The necessary dataset derived from the vowel and word speech tokens was utilized for the analysis of the convolutional neural network. Then the model was trained and validated for both of the isolated vowels and words separately for the same number of data. The performance was measured according to four different metrics- loss, accuracy, confusion matrix, and cross-validation score. In all these cases, the performance of vowel recognition has been found superior to word recognition. The reason behind this performance variation has been studied and found that it is mostly related to the dynamic variation of the vocal tract between vowels and words at the time of speaking. MFCC is chosen as the feature of interest for classification purposes. The variation of MFCC for vowels and words have been compared and found that MFCCs of words have more variation than the vowels. As a consequence, it is concluded that the dynamic variation of the vocal tract is inversely related to the performance of recognition.

If you use the dataset or any of the codes in this repository, please cite the following paper as appropriate:
```bibtex
@inproceedings{hasan2020investigation,
    title={Investigation of the Effect of {MFCC} Variation on the Convolutional Neural Network-Based Speech Classification},
    author={Hasan, Md Rakibul and Hasan, Md Mahbub},
    booktitle={2020 IEEE Region 10 Symposium (TENSYMP)},
    pages={1408--1411},
    year={2020},
    organization={IEEE},
    doi={10.1109/TENSYMP50017.2020.9230697}
}
```

**Note: It's compatible with TensorFlow 1.x**

**Follow-up project:** [https://github.com/hasan-rakibul/bengali-vowels-words-classification](https://github.com/hasan-rakibul/bengali-vowels-words-classification)