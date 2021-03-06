# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.

import os
import unittest

from cdm.enums import CdmStatusLevel

from tests.cdm.projection.attribute_context_util import AttributeContextUtil
from tests.common import async_test, TestHelper, TestUtils


class ForwardCompatibilityTest(unittest.TestCase):
    """Tests all the projections will not break the OM even if not implemented."""

    # The path between TestDataPath and TestName.
    tests_subpath = os.path.join('Cdm', 'Projection', 'TestForwardCompatibility')

    @async_test
    async def test_all_operations(self):
        """Tests running all the projections (includes projections that are not implemented)."""
        test_name = 'TestAllOperations'
        entity_name = test_name
        corpus = TestHelper.get_local_corpus(self.tests_subpath, test_name)

        def callback(level: CdmStatusLevel, message: str):
            if message.find('Projection operation not implemented yet.') == -1:
                self.fail('Some unexpected failure - {}!'.format(message))
        corpus.set_event_callback(callback, CdmStatusLevel.ERROR)
        expected_output_path = TestHelper.get_expected_output_folder_path(self.tests_subpath, test_name)

        ent_test_entity_string_reference = await corpus.fetch_object_async('local:/{0}.cdm.json/{0}'.format(entity_name))  # type: CdmEntityDefinition
        self.assertIsNotNone(ent_test_entity_string_reference)
        resolved_test_entity_string_reference = await TestUtils._get_resolved_entity(corpus, ent_test_entity_string_reference, ['referenceOnly'])  # type: CdmEntityDefinition
        self.assertIsNotNone(resolved_test_entity_string_reference)
        AttributeContextUtil.validate_attribute_context(self, corpus, expected_output_path, entity_name, resolved_test_entity_string_reference)
