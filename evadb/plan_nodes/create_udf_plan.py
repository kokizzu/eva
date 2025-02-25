# coding=utf-8
# Copyright 2018-2023 EvaDB
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
from pathlib import Path
from typing import List

from evadb.catalog.models.udf_io_catalog import UdfIOCatalogEntry
from evadb.catalog.models.udf_metadata_catalog import UdfMetadataCatalogEntry
from evadb.plan_nodes.abstract_plan import AbstractPlan
from evadb.plan_nodes.types import PlanOprType


class CreateUDFPlan(AbstractPlan):
    """
    This plan is used for storing information required to create udf operators

    Attributes:
        name: str
            udf_name provided by the user required
        if_not_exists: bool
            if true should throw an error if udf with same name exists
            else will replace the existing
        inputs: List[UdfIOCatalogEntry]
            udf inputs, annotated list similar to table columns
        outputs: List[UdfIOCatalogEntry]
            udf outputs, annotated list similar to table columns
        impl_file_path: Path
            file path which holds the implementation of the udf.
        udf_type: str
            udf type. it ca be object detection, classification etc.
    """

    def __init__(
        self,
        name: str,
        if_not_exists: bool,
        inputs: List[UdfIOCatalogEntry],
        outputs: List[UdfIOCatalogEntry],
        impl_file_path: Path,
        udf_type: str = None,
        metadata: List[UdfMetadataCatalogEntry] = None,
    ):
        super().__init__(PlanOprType.CREATE_UDF)
        self._name = name
        self._if_not_exists = if_not_exists
        self._inputs = inputs
        self._outputs = outputs
        self._impl_path = impl_file_path
        self._udf_type = udf_type
        self._metadata = metadata

    @property
    def name(self):
        return self._name

    @property
    def if_not_exists(self):
        return self._if_not_exists

    @property
    def inputs(self):
        return self._inputs

    @property
    def outputs(self):
        return self._outputs

    @property
    def impl_path(self):
        return self._impl_path

    @property
    def udf_type(self):
        return self._udf_type

    @property
    def metadata(self):
        return self._metadata

    def __str__(self):
        return "CreateUDFPlan(name={}, \
            if_not_exists={}, \
            inputs={}, \
            outputs={}, \
            impl_file_path={}, \
            udf_type={}, \
            metadata={})".format(
            self._name,
            self._if_not_exists,
            self._inputs,
            self._outputs,
            self._impl_path,
            self._udf_type,
            self._metadata,
        )

    def __hash__(self) -> int:
        return hash(
            (
                super().__hash__(),
                self.if_not_exists,
                tuple(self.inputs),
                tuple(self.outputs),
                self.impl_path,
                self.udf_type,
                tuple(self.metadata),
            )
        )
