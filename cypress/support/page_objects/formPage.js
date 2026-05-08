class FormPage {
  llenarFormulario(nombre, apellido, ciudad) {
    if (nombre) {
      cy.get('input[name="nombre"]').clear().type(nombre);
    }
    if (apellido) {
      cy.get('input[name="apellido"]').clear().type(apellido);
    }
    if (ciudad) {
      cy.get('input[name="ciudad"]').clear().type(ciudad);
    }
    return this;
  }

  guardar() {
    cy.get('button[type="submit"]').click();
  }
}

export const formPage = new FormPage();