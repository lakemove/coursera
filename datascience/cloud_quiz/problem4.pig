register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-*' USING TextLoader as (line:chararray);

ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

subjects = group ntriples by (subject) PARALLEL 50;

subject_count = foreach subjects generate group as subject, COUNT($1) as count PARALLEL 50;

group_subject_count = group subject_count by (count) PARALLEL 50;

count_grp_sub = foreach group_subject_count generate group as subcount, COUNT($1) as grpcount PARALLEL 50;



store count_grp_sub into '/user/hadoop/distribution-result' using PigStorage();
-- Alternatively, you can store the results in S3, see instructions:
-- store count_by_object_ordered into 's3n://superman/example-results';