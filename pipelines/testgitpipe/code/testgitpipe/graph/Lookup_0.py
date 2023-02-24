from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.libs import typed_lit
from testgitpipe.config.ConfigStore import *
from testgitpipe.udfs.UDFs import *

def Lookup_0(spark: SparkSession, in0: DataFrame):
    keyColumns = []
    valueColumns = []
    createLookup("", in0, spark, keyColumns, valueColumns)
