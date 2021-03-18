#!/usr/bin/env python

"""Tests for `octis` package."""

import pytest

from click.testing import CliRunner
from octis.evaluation_metrics.classification_metrics import F1Score

from octis.evaluation_metrics.coherence_metrics import *
from octis.dataset.dataset import Dataset
from octis.models.LDA import LDA
from octis.models.ETM import ETM
from octis.models.CTM import CTM
from octis.models.NMF import NMF
from octis.models.NMF_scikit import NMF_scikit
from octis.models.ProdLDA import ProdLDA

import os
from octis.preprocessing.preprocessing import Preprocessing


@pytest.fixture
def root_dir():
    return os.path.dirname(os.path.abspath(__file__))


@pytest.fixture
def data_dir(root_dir):
    return root_dir + "/../preprocessed_datasets/"


def test_preprocessing(data_dir):
    texts_path = data_dir+"/sample_texts/unprepr_docs.txt"
    p = Preprocessing(vocabulary=None, max_features=None, remove_punctuation=True, punctuation=".,?:",
                      lemmatize=True, remove_stopwords=True, stopword_list=['am', 'are', 'this', 'that'],
                      min_chars=1, min_words_docs=0,)
    dataset = p.preprocess_dataset(
        documents_path=texts_path,
    )

    dataset.save(data_dir+"/sample_texts")
    dataset.load_custom_dataset(data_dir+"/sample_texts")



def test_load_20ng():
    dataset = Dataset()
    dataset.fetch_dataset("20NewsGroup")
    assert len(dataset.get_corpus()) == 16310


def test_load_M10():
    dataset = Dataset()
    dataset.fetch_dataset("M10")
    assert len(dataset.get_labels()) == 10
