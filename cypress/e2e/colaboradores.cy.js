import { indexPage } from "../support/page_objects/indexPage";
import { formPage } from "../support/page_objects/formPage";

describe('Pruebas del CRUD de Colaboradores (Patrón POM + Fixtures)', () => {
  
  beforeEach(() => {
    indexPage.visit();
  });

  it('Debe completar el ciclo de vida del colaborador (Crear, Editar, Eliminar)', () => {
    
    cy.fixture('colaborador.json').then((datos) => {
      
      // --- 1. CREAR (CREATE) ---
      indexPage.clickNuevoRegistro();
      cy.url().should('include', '/create');
      
      // Funcion para llenar formulario
      formPage.llenarFormulario(datos.nombre, datos.apellido, datos.ciudad)
              .guardar();
      
      // Funcion para verificar que el colaborador se creó correctamente
      indexPage.verificarColaboradorExiste(datos.nombre, datos.ciudad);
  
      // --- 2. EDITAR (UPDATE) ---
      indexPage.clickEditar(datos.nombre);
      cy.url().should('include', '/edit');
  
      // Modificamos solo el nombre y la ciudad, dejando el apellido igual
      formPage.llenarFormulario('Carlos Manuel', null, 'Santiago')
              .guardar();
  
      indexPage.verificarColaboradorExiste('Carlos Manuel', 'Santiago');
  
      // --- 3. ELIMINAR (DELETE) ---
      indexPage.clickEliminar('Carlos Manuel');
      indexPage.verificarColaboradorNoExiste('Carlos Manuel');
    });

  });
});