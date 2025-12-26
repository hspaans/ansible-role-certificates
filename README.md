# Role Name

> [!WARNING]
> As manual certificates have been replaced by [Let's Encrypt](https://github.com/letsencrypt) and this role has been archived.

Push X.509 certificates to servers and using the structure from certbot for deployment.

## Requirements

None.

## Role Variables

Default variables are set in `defaults/main.yml`.

## Dependencies

No dependency on other Ansible Galaxy roles.

## Example Playbook

    - hosts: servers
      vars:
        certificates_private:
          - name: www.example.org
            cert: !vault |
              $ANSIBLE_VAULT;1.1;AES256
              62663162646531663532611139313861653138656136313135385312643435613463623438633837
            chain: !vault |
              $ANSIBLE_VAULT;1.1;AES256
              62663162646531663532611139313861653138656136313135385312643435613463623438633837
            fullchain: !vault |
              $ANSIBLE_VAULT;1.1;AES256
              62663162646531663532611139313861653138656136313135385312643435613463623438633837
            privkey: !vault |
              $ANSIBLE_VAULT;1.1;AES256
              62663162646531663532611139313861653138656136313135385312643435613463623438633837
          - name: mail.example.org
            cert: !vault |
              $ANSIBLE_VAULT;1.1;AES256
              62663162646531663532611139313861653138656136313135385312643435613463623438633837
            chain: !vault |
              $ANSIBLE_VAULT;1.1;AES256
              62663162646531663532611139313861653138656136313135385312643435613463623438633837
            fullchain: !vault |
              $ANSIBLE_VAULT;1.1;AES256
              62663162646531663532611139313861653138656136313135385312643435613463623438633837
            privkey: !vault |
              $ANSIBLE_VAULT;1.1;AES256
              62663162646531663532611139313861653138656136313135385312643435613463623438633837
      roles:
        - { role: hspaans.certificates, become: true }

## License

MIT

## Author Information

This role was created in 2020 by [Hans Spaans](https://github.com/hspaans).
