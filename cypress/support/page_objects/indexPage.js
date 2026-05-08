class IndexPage {
  visit() {
    cy.visit('http://127.0.0.1:5000/');
    return this;
  }

  clickNuevoRegistro() {
    cy.contains('Nuevo Registro').click();
  }

  buscarColaborador(nombre) {
    return cy.contains('td', nombre).parent('tr');
  }

  clickEditar(nombre) {
    this.buscarColaborador(nombre).contains('Editar').click();
  }

  clickEliminar(nombre) {
    cy.on('window:confirm', () => true);
    this.buscarColaborador(nombre).contains('Eliminar').click();
  }

  verificarColaboradorExiste(nombre, ciudad) {
    cy.contains(nombre).should('be.visible');
    if (ciudad) {
      cy.contains(ciudad).should('be.visible');
    }
  }

  verificarColaboradorNoExiste(nombre) {
    cy.contains(nombre).should('not.exist');
  }
}

export const indexPage = new IndexPage();