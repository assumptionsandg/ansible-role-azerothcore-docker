# azerothcore_user

Create users via the AzerothCore SOAP API.

This role manages users, including passwords and admin status. This role
requires a bootstrap user to be configured. If no password for the bootstrap
user is set the role will prompt for one to be defined before continuing. 

The default username for the bootstrap username for the bootstrap user is
`acaboostrap`... this can be changed by `azerothcore_user_bootstrap_username`:

```yaml
azerothcore_user_bootstrap_username: acabootstrap
azerothcore_user_bootstrap_password: <vault_encrypted_password>

```

The list of users to be created can be set in the `azerothcore_user_list` dict:

```yaml
azerothcore_user_list:
  admin:
    enabled: true
    gmlevel: 1
    password: <vault_encrypt_string>

```

See the collection README for supported variables.

## License

GPL-3.0-only
