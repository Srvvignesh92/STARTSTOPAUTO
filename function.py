
import boto3
import os

v1="AutoStart"
v2="True"

def rds_stop():
    #response=print(" *****   Start of the code to check the rds instance  **** ")
    region=os.environ['AWS_REGION']
   
  
    client = boto3.client('rds', region_name=region)
    response=client.describe_db_instances()
    #print(response)
    for db in response['DBInstances']:
        print(db['DBInstanceIdentifier'])
        dbname=db['DBInstanceIdentifier']
    #    print(dbname)
    #    print(db['DBInstanceArn'])
        arn=db['DBInstanceArn']
        print(arn)
        tag=client.list_tags_for_resource(ResourceName=arn)
        print(tag)
        for val in tag['TagList']:
            Ky=val['Key']
            Ve=val['Value']
    #        print(Ky)
    #        print(Ve)
            if Ky == v1 and Ve == v2:
                print("this db is autostart")
                stop=client.start_db_instance(DBInstanceIdentifier=dbname)
            else:
                print("this db is not autostart")
           
        
            
                
        
        #stop=client.stop_db_instance(DBInstanceIdentifier=dbname)
    #response = client.describe_db_instances(DBInstanceIdentifier='*')
    #response = client.list_tags_for_resource(ResourceName='arn:aws:rds:eu-west-2:502511304737:db:test-rds')
    #print(response)
    
    return(response)
   




def lambda_handler(event, context):
    rds_stop()
    
