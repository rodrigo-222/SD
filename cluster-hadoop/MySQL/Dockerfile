# Use a imagem oficial do MySQL
FROM mysql:latest

# Define variáveis de ambiente para a configuração do MySQL
ENV MYSQL_ROOT_PASSWORD=root
ENV MYSQL_DATABASE=DB

# Adiciona o script de inicialização do banco de dados
ADD setup.sql /home/rodrigo/cluster-hadoop/MySQL/