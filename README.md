## Schema checker for DDE-compatibility
#### Note that as of April, 2022, this repository is no longer needed/useful. Many of the issues caused by differences in the strictness of the DDE in validating schemas vs creating them have been addressed. This repository remains for archival purposes only.

The Data Discovery Engine's Schema Playground is very strict when ingesting and displaying schemas, but more flexible when creating them. As a result, it is possible to use the Schema Playground to create a schema that would not be viewable in the playground's schema viewer.

This script uses github actions to automatically fix a known source of occasional "internal error" in schemas so that they can be viewed with the schema viewer. This error occassionally happens with the creation of properties expecting/referencing non-schema.org classes. This script creates a dummy class so that that the DDE schema playground viewer can bypass this issue.

This script does NOT address other issues with json schema validation

### To use:
1. Fork this repo
2. Create your schema in the Data Discovery Engine (DDE), and save it to the `drafts` folder in your fork of this repo
3. View your schema in the DDE schema viewer. If it works, you don't need this repo.
4. Github actions should run the script and generate dummy classes as needed. These will be saved/committed to the `edited` folder
5. Check to see if your schema works in the DDE schema viewer.
6. If it does not, you may find other sources of error by using https://www.jsonschemavalidator.net/
