# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import unittest
from sslyze.plugins.session_renegotiation_plugin import SessionRenegotiationPlugin, SessionRenegotiationScanCommand
from sslyze.server_connectivity import ServerConnectivityInfo


class SessionRenegotiationPluginTestCase(unittest.TestCase):

    def test_renegotiation_good(self):
        server_info = ServerConnectivityInfo(hostname='www.google.com')
        server_info.test_connectivity_to_server()

        plugin = SessionRenegotiationPlugin()
        plugin_result = plugin.process_task(server_info, SessionRenegotiationScanCommand())

        self.assertFalse(plugin_result.accepts_client_renegotiation)
        self.assertTrue(plugin_result.supports_secure_renegotiation)

        self.assertTrue(plugin_result.as_text())
        self.assertTrue(plugin_result.as_xml())

    def test_renegotiation_bad(self):
        # TBD
        pass