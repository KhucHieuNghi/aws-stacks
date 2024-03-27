# Quokka Test

## Video demo
    attached in github demo.mov

## Stacks
    aws-stacks: Lambda, Dynamodb, Cloudwatch

## CURL APIs
    attached in github "thunder-collection_api.json" by thunder tool

1. Get All & By UserName 
username can empty, pagesize default 5, page default 1
```
    curl  -X POST \
    'https://f4nb4z7p6bbhyokfiimba3ieti0gecvd.lambda-url.us-east-1.on.aws/' \
    --header 'Content-Type: application/json' \
    --data-raw '{
        "method": "GET",
        "query": {
            "username": "",
            "page": 1
        }
    }'
```

2. Create Note
content and username can not empty
```
   curl  -X POST \
        'https://f4nb4z7p6bbhyokfiimba3ieti0gecvd.lambda-url.us-east-1.on.aws/' \
        --header 'Content-Type: application/json' \
        --data-raw '{
        "method": "GET",
        "body": {
            "content": "nk + 3",
            "username": "nk"
        }
    }'
```

3. Response note type 
```
{
    "id": "8991a930-b6b7-4cd8-8776-245867c9d168",
    "content": "note",
    "username": "nk",
    "timestamp": 1711567774
}
```

## Codebase testing
>> make be-mock (follow makefile)
>> make be-test (follow makefile)
### Plan testing
> Unit test common function
> Testing validation of function
```
    If GET method can empty params
    If POST method body can not miss (content and username)
```
> make be-test (follow makefile)

## CI & CD
Flows (BE): Stacks by github-action and CDK
    workspace ./aws
> setup env & platform python >= 3.6 & node >= 18.x
> install CDK (aws) and credentials
> Testing codebase with command ``` make be-test ```
> Testing codebase with cdk command: ``` cdk synth ```
> bootstrap cdk to Bundle/Build 
> (CD) Deployment to AWS with cdk

Flows (FE): Stack by Vercel
    workspace ./fe
> setup env & node >= 18.x
> testing bundle
> build image
> deployment to Vercel


## A brief outline of your approach (how to implement)
1. Focus main feature note (Create note, Filter note)
2. Define scheme database
3. Define fields can filter and pagination

4. [BE] Setup localstacks to implement aws-stacks at local

5. [BE] Setup AWS env
6. [BE] Implement codebase CDK & Testing deployment from local
7. [BE] Implement features
8. [BE] Code testing feature

9. [FE] Setup FE env
10. [FE] Implement UI
11.[FE] Integration APIs

11. [FE][BE] Deployment production

12. Document

## How much time you spent on which aspects of the application

setup AWS take-time 2h
mindful to coding backend 4h, frontend 2h, document and deployment 2h => 10h

## Limit
### at CI
I have experience using CDK before, however, using cdk from aws is very strict from setup to deployment. It takes more time and effort to deploy and there will be many other risks related to the back compatibility of the CDK.

### development
Also another problem from aws, the current aws stacks I am using localstack to make local deployment easier however this will cause back compatity


## How to run local
FE
> cd to workspace ./fe
> yarn
> yarn dev

BE
> follow makefile 
> make be-setup
> cd workspace ./aws 
> docker compose up to setup localstack
> make be-dev
> make testing

## Domains
BE: https://f4nb4z7p6bbhyokfiimba3ieti0gecvd.lambda-url.us-east-1.on.aws
FE: https://f4nb4z7p6bbhyokfiimba3ieti0gecvd.lambda-url.us-east-1.on.aws
