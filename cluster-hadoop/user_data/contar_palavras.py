import findspark
from pyspark.sql.session import SparkSession
from pyspark import SparkContext, SparkConf

# Inicializando Spark
findspark.init("/usr/spark-3.5.1/")

spark = (
    SparkSession.builder.appName("sparksubmit_test_app")
    .config("spark.sql.warehouse.dir", "hdfs:///user/hive/warehouse")
    .config("spark.sql.catalogImplementation", "hive")
    .getOrCreate()
)

# criar um contexto de sessão do spark (cria um "programa")
sc = SparkContext.getOrCreate()



def main():

    df = spark.read.text("hdfs://spark-master:9000/datasets/")  # noqa: F841

    # variável recebe o caminho que aponta para uma arquivo de texto
    file_path = "/datasets/*.txt"
    # leitura do arquivo de texto pelo programa spark
    words = sc.textFile(f"{file_path}").flatMap(lambda line: line.split(" "))
    # contagem de palavras utilizando a sintaxe facilitada do pyspark
    wordCounts = words.map(lambda word: (word, 1)).reduceByKey(lambda a,b:a +b)
    # salvando arquivo com resultado da execução
    wordCounts.saveAsTextFile(f"{'/'.join(file_path.split('/')[:-1])}/word_count")
   
    print(wordCounts.count())
    print(wordCounts.countApproxDistinct())


if __name__ == "__main__":
    main()



spark.stop()