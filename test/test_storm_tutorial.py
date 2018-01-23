import synapse.cortex as s_cortex
from synapse.lib.iq import SynTest

CORE_URL = '/storm-tutorial/tutorial-core.db'


class StormTutorialTest(SynTest):

    def test_ingest_example_fqdns(self):
        with s_cortex.openurl('sqlite:///' + CORE_URL) as core:
            self.nn(core.getTufoByProp('inet:fqdn', 'example.com'))
            self.nn(core.getTufoByProp('inet:fqdn', 'com'))
            self.nn(core.getTufoByProp('inet:fqdn', 'vertex.link'))
            self.nn(core.getTufoByProp('inet:fqdn', 'link'))
            self.nn(core.getTufoByProp('inet:fqdn', 'localhost'))

    def test_ingest_example_ips(self):
        with s_cortex.openurl('sqlite:///' + CORE_URL) as core:
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.0'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.1'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.2'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.3'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.4'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.5'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.6'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.7'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.8'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.9'))
            self.nn(core.getTufoByProp('inet:ipv4', '192.168.0.10'))
