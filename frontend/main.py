import streamlit as st
from aws.client import S3Client
from datasource.csv import CSVCollector
from contract.catalogo import Catalogo

st.title('Essa é uma página de portal de dados')

aws = S3Client()
catalogo = CSVCollector(Catalogo, aws)
catalogo.start()