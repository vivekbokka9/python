import boto3

def lambda_handler(event, context):

    account_id = boto3.client('sts').get_caller_identity().get('Account')
    ec2 = boto3.client('ec2')
    regions = [region['RegionName']
               for region in ec2.describe_regions()['Regions']]

    for region in regions:
        print('Region:', region)
        ec2 = boto3.client('ec2', region_name=region)

        response = ec2.describe_snapshots(OwnerIds=[account_id])
        snapshots = response["Snapshots"]

        snapshots.sort(key=lambda x: x["StartTime"])

        snapshots = snapshots[:-5]

        for snapshot in snapshots:
            id = snapshot['SNapshotId']
            try:
                print("Deleting Snapshot:", id)
                ec2.delete_snapshots(SnapshotId=id)
            except Exception as e:
                if 'InvalidSnapshot.InUse' in e.message:
                    print("Snapshot {} in use, skipping.".format(id))
                    continue