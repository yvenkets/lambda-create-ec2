import boto3
dryRun = False; # useful variable to put the script into dry run mode where the function allows it

ec2Client = boto3.client('ec2')
ec2Resource = boto3.resource('ec2')

# Create the instance
instanceDict = ec2Resource.create_instances(
    DryRun = dryRun,
    ImageId = "ami-04893cdb768d0f9ee",
    KeyName = "Prod",
    InstanceType = "t2.micro",
    SecurityGroupIds = ["sg-00be94ecc8ad7ade5"],
    MinCount = 1,

)
# Wait for it to launch before assigning the elastic IP address
instanceDict[0].wait_until_running();

# Allocate an elastic IP
#eip = ec2Client.allocate_address(DryRun=dryRun, Domain='vpc')
# Associate the elastic IP address with the instance launched above
ec2Client.associate_address(
     DryRun = dryRun,
     InstanceId = instanceDict[0].id,
     AllocationId = "eipalloc-01f8600a40ff4e77c" )
