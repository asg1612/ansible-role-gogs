import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_gogs_socket(host):
    assert host.socket("tcp://0.0.0.0:10080").is_listening
    assert host.socket("tcp://0.0.0.0:10022").is_listening
