# Migration To Version v.1.0.0

Since v1 uses a new setup procedure, a migration is necessary from v0. Follow the
steps below to migrate from v0 to v1.

- **Step 1:** Rename the existing project from "fpack_webapp_client" to
  "fpack_webapp_client_old". Make sure it stays in the same parent directory.
- **Step 2:** Open a terminal or Git Bash, navigate to the directory where the
  existing project is stored, and clone the latest repository using the command:
  ```
  git clone https://github.com/btamm12/fpack_webapp_client.git
  ```
- **Step 3:** Run the following commands to perform the migration:
  ```
  cd fpack_webapp_client
  bash ./make_environment.sh
  bash ./make_migration.sh
  ```
- **Step 4:** If the migration is successful, all of your data will have moved to the
  new repository. In this case, you can delete the old repository
  "fpack_webapp_client_old".

