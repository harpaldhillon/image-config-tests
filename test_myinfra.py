import subprocess

def test_passwd_file(host):
    passwd = host.file("/etc/passwd")
    assert passwd.contains("root")
    assert passwd.user == "root"
    assert passwd.group == "root"
    assert passwd.mode == 0o644

def test_openssh_clients_package_not_installed(host):
    # Check if the nftables package is not installed
    assert not host.package("openssh-clients").is_installed, "openssh clients package should not be installed"

def test_nftables_package_not_installed(host):
    # Check if the nftables package is not installed
    assert not host.package("nftables").is_installed, "nftables package should not be installed"

def test_rsync_package_not_installed(host):
    # Check if the rsync package is not installed
    assert not host.package("rsync").is_installed, "rsync package should not be installed"

def test_stat_tmp_uid(host):
    # Run the command "stat /tmp|grep Uid"
    cmd_result = host.run("stat /tmp | grep Uid")

    # Check the output to verify the Uid information
    assert "Uid:" in cmd_result.stdout, "Uid information not found in the output"

def test_vsftpd_package_not_installed(host):
    # Check if the rsync package is not installed
    assert not host.package("vsftpd").is_installed, "vsftpd package should not be installed"


def test_bind_package_not_installed(host):
    # Check if the rsync package is not installed
    assert not host.package("bind").is_installed, "bind package should not be installed"

def test_bind_package_not_installed(host):
    # Check if the rsync package is not installed
    assert not host.package("bind").is_installed, "bind package should not be installed"

def test_root_group_gid(host):
    # Get root user and group information
    root_user = host.user("root")
    root_group = host.group("root")

    print(root_user.gid)

    # Check if the root user's primary group GID is not 0
    assert root_user.gid == 0, "Default group for root account should be GID 0"

    # Check if the root group's GID is 0
    assert root_group.gid == 0, "Root group's GID should be 0"

def test_stat_passwd_uid(host):
    # Run the command "stat /etc/passwd|grep Uid"
    cmd_result = host.run("stat /etc/passwd | grep Uid")

    # Check the output to verify the Uid information
    assert "Uid:" in cmd_result.stdout, "Uid information not found in the output"

def test_root_account_not_locked(host):
    # Get the contents of the /etc/shadow file
    shadow_contents = host.file("/etc/shadow").content_string

    # Find the root account entry and check if it's not locked
    root_account_entry = next((line for line in shadow_contents.splitlines() if line.startswith("root:")), None)
    assert root_account_entry is not None, "Root account entry not found in /etc/shadow"
    assert "!" in root_account_entry, "Root account should not be locked in /etc/shadow"

