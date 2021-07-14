# coding=utf-8
# Copyright 2020 The HuggingFace Datasets Authors and the current dataset script contributor.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""RAFT submission"""


import csv
import datasets


# TODO: Add BibTeX citation
# Find for instance the citation on arxiv or on the dataset repo/website
_CITATION = """\
@InProceedings{huggingface:dataset,
title = {A great new dataset},
author={huggingface, Inc.
},
year={2020}
}
"""

# You can copy an official description
_DESCRIPTION = """\
This dataset contains a corpus of AI papers. The first task is to determine\
 whether or not a datapoint is an AI safety paper. The second task is to\
 determine what type of paper it is.
"""

# TODO: Add a link to an official homepage for the dataset here
_HOMEPAGE = ""

# TODO: Add the licence for the dataset here if you can find it
_LICENSE = ""


class RaftSubmission(datasets.GeneratorBasedBuilder):
    """Load predictions on RAFT benchmark"""

    VERSION = datasets.Version("1.1.0")
    BUILDER_CONFIGS = [
        datasets.BuilderConfig(
            name="safety_or_not", version=VERSION, description="Decide whether the papers focus on AI safety methods."
        ),
    ]

    def _info(self):
        if self.config.name == "safety_or_not":
            features = datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "label": datasets.ClassLabel(names=["Not safety", "Safety"]),
                }
            )
        else:
            features = datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "label": datasets.Value("string"),
                }
            )
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=features,
            supervised_keys=None,
            homepage=_HOMEPAGE,
            license=_LICENSE,
            citation=_CITATION,
        )

    def _split_generators(self, dl_manager):
        filepath = dl_manager.download_and_extract(f"{self.config.name}.csv")
        return [datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": filepath})]

    def _generate_examples(self, filepath):
        with open(filepath, encoding="utf-8") as f:
            csv_reader = csv.reader(f, quotechar='"', delimiter=",", quoting=csv.QUOTE_ALL, skipinitialspace=True)
            for id_, row in enumerate(csv_reader):
                if id_ == 0:  # First row is column names
                    continue
                id, label = row
                yield id_, {"id": id, "label": label}
