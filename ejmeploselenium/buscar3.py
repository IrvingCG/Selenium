import unittest
from selenium import webdriver
import buscar3

class PythonOrgSearch(unittest.TestCase):
    """Una clase de prueba de ejemplo para mostrar cómo funciona el objeto de página"""

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """Prueba python.org función de búsqueda. Busca la palabra "pycon" entonces
            Se ha verificado que aparecen algunos resultados. Tenga en cuenta que no busca
            cualquier texto en particular en la página de resultados de búsqueda. Esta prueba verifica que:
            Los resultados no fueron vacíos.."""

        #Carga la página principal. En este caso, la página de inicio de Python.org.
        main_page = buscar3.MainPage(self.driver)
        #Comprueba si la palabra "Python" está en el título
        self.assertTrue(main_page.is_title_matches(), "python.org title doesn't match.")
        #Establece el texto del cuadro de texto de búsqueda en "pycon"
        main_page.search_text_element = "pycon"
        main_page.click_go_button()
        search_results_page = buscar3.SearchResultsPage(self.driver)
        #Verifica que la página de resultados no esté vacía
        self.assertTrue(search_results_page.is_results_found(), "No results found.")

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()