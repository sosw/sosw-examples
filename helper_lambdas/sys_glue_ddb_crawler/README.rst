sys-glue-ddb-crawler
----------------------

We introduce a new helper function that can automatically create and update Schemas of existing DynamoDB Tables
in your AWS Glue Data Catalog.

`See full documentation <https://docs.sosw.app/tools/ddb_glue_crawler.html>`_

To install this function clone the repository, go to the relevant directory and use SAM.

..  warning::

    Replace the ``SOSW_LAYER_PLACEHOLDER`` with the latest version of your ``sosw`` Layer.

..  code-block:: bash

    cd helper_lambdas/sys_glue_ddb_crawler
    sam build && sam deploy

To manually invoke the function:

..  code-block:: bash

    aws lambda invoke --function-name sys-glue-ddb-crawler --payload '{}' /tmp/sys-glue-ddb-crawler.log

