from report_generator_interface import ReortGeneratorInterface


class CsvReortGenerator(ReortGeneratorInterface):

    def generate(self):
        # codigo para gerar o report em csv

        return 'report.csv' # retorna o nome do arquivo e o caminho onde ele foi salvo
