While in the same folder as your ``depoy.sh`` file just run:
    ./deploy.sh [-v branch] [-p profile]

After pack a new layer in zip archive and put it in your S3 bucket. 

To deploy with CloudFormation use [sosw.yaml] to create a stack run :
    ``aws cloudformation create-stack \
      --stack-name myteststack \
      --template-body file:///home/testuser/mytemplate.json \
      --parameters ParameterKey=Parm1,ParameterValue=test1 ParameterKey=Parm2,ParameterValue=test2``

Or upload it directly via GUI.

To deploy with AWS SAM use [samconfig.toml] and [template.yaml]

In the same folder run ``sam build && sam deploy``

Don't forget to change placeholders like ``{FileName}`` with your actual data.
