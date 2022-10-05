var cedula = null;
var nombre = null;
var apellido = null;
var fecha = null;
var correo = null;
var celular = null;

function limpiarCamposCrear() {
  var cedula = document.getElementById("cedulaCrear");
  var nombre = document.getElementById("nombreCrear");
  var apellido = document.getElementById("apellidoCrear");
  var fecha = document.getElementById("fechaCrear");
  var correo = document.getElementById("correoCrear");
  var celular = document.getElementById("celularCrear");
  cedula.value = ""
  nombre.value = ""
  apellido.value = ""
  fecha.value = ""
  correo.value = ""
  celular.value = ""
}

function registrarPersona() {
  cedula = document.getElementsByName("cedula")[0].value;
  nombre = document.getElementsByName("nombre")[0].value;
  apellido = document.getElementsByName("apellido")[0].value;
  fecha = document.getElementsByName("fecha")[0].value;
  correo = document.getElementsByName("correo")[0].value;
  celular = document.getElementsByName("celular")[0].value;
  axios.post('http://127.0.0.1:8000/persona/crear/', {

    cc: cedula,
    nombre1: nombre,
    apellido1: apellido,
    fecha: fecha,
    correo: correo,
    celular: celular,
  })
    .then(function (response) {
      console.log(response);
      
    })
    .catch(function (error) {
      console.log(error);
     
    });
    limpiarCamposCrear();
}


function crearEncabezado() {
  for (let filas = 0; filas < 1; filas++) {
    let filaActual = document.getElementById("listarPersonas").insertRow(filas);
    for (let columnas = 0; columnas < 6; columnas++) {
      let celda = filaActual.insertCell(columnas);
      if (columnas == 0) {
        celda.innerHTML = 'Cedulas';
      } else if (columnas == 1) {
        celda.innerHTML = 'Nombres';
      } else if (columnas == 2) {
        celda.innerHTML = 'Apellidos';
      } else if (columnas == 3) {
        celda.innerHTML = 'Fechas';
      } else if (columnas == 4) {
        celda.innerHTML = 'Correos';
      } else if (columnas == 5) {
        celda.innerHTML = 'Telefonos';
      }
    }
  }
}

function limpiar() {
  document.getElementById("listarPersonas").innerHTML = '';
}

function consultarDatos() {
  // Make a request for a user with a given ID
  axios.get("http://127.0.0.1:8000/persona/listar/")
    .then(resp => {
      console.log(resp.data);
      limpiar();
      var contador = 0;
      var bandera = true;
      while (bandera === true) {
        if (resp.data[contador] != undefined) {
          contador++;
        } else {
          bandera = false;
        }
      }
      for (let filas = 0; filas < contador; filas++) {
        let filaActual = document.getElementById("listarPersonas").insertRow(filas);
        for (let columnas = 0; columnas < 6; columnas++) {
          let celda = filaActual.insertCell(columnas);
          if (columnas == 0) {
            celda.innerHTML = resp.data[filas].cc;
          } else if (columnas == 1) {
            celda.innerHTML = resp.data[filas].nombre1;
          } else if (columnas == 2) {
            celda.innerHTML = resp.data[filas].apellido1;
          } else if (columnas == 3) {
            celda.innerHTML = resp.data[filas].fecha;
          } else if (columnas == 4) {
            celda.innerHTML = resp.data[filas].correo;
          } else if (columnas == 5) {
            celda.innerHTML = resp.data[filas].celular;
          }

        }

      }
      crearEncabezado();
    });
}

function obtenerDatos() {
  cedula = document.getElementsByName("cedulafiltrar")[0].value;
  // Make a request for a user with a given ID
  axios.get("http://127.0.0.1:8000/persona/listar/" + cedula + "/")
    .then(resp => {
      console.log(resp.data);
      var cedula = document.getElementById("cedulaActualizar");
      var nombre = document.getElementById("nombreActualizar");
      var apellido = document.getElementById("apellidoActualizar");
      var fecha = document.getElementById("fechaActualizar");
      var correo = document.getElementById("correoActualizar");
      var celular = document.getElementById("celularActualizar");
      cedula.value = resp.data.cc;
      nombre.value = resp.data.nombre1
      apellido.value = resp.data.apellido1
      fecha.value = resp.data.fecha
      correo.value = resp.data.correo
      celular.value = resp.data.celular
    });
}

function limpiarCamposActualizar() {
  var cedula = document.getElementById("cedulaActualizar");
  var nombre = document.getElementById("nombreActualizar");
  var apellido = document.getElementById("apellidoActualizar");
  var fecha = document.getElementById("fechaActualizar");
  var correo = document.getElementById("correoActualizar");
  var celular = document.getElementById("celularActualizar");
  cedula.value = ""
  nombre.value = ""
  apellido.value = ""
  fecha.value = ""
  correo.value = ""
  celular.value = ""
}

function ModificarPersona() {
  var cedulaFiltrada = document.getElementsByName("cedulafiltrar")[0].value;
  var cedula = document.getElementsByName("cedulaActualizar")[0].value;
  var nombre = document.getElementsByName("nombreActualizar")[0].value;
  var apellido = document.getElementsByName("apellidoActualizar")[0].value;
  var fecha = document.getElementsByName("fechaActualizar")[0].value;
  var correo = document.getElementsByName("correoActualizar")[0].value;
  var celular = document.getElementsByName("celularActualizar")[0].value;
  axios.put("http://127.0.0.1:8000/persona/actualizar/" + cedulaFiltrada + "/", {
    cc: cedulaFiltrada,
    nombre1: nombre,
    apellido1: apellido,
    fecha: fecha,
    correo: correo,
    celular: celular
  })
    .then(function (response) {
      console.log(response);
      limpiarCamposActualizar();
    })
    .catch(function (error) {
      console.log(error);
    });
}

function obtenerDatos2() {
  cedula = document.getElementsByName("cedulafiltrar2")[0].value;
  // Make a request for a user with a given ID
  axios.get("http://127.0.0.1:8000/persona/listar/" + cedula + "/")
    .then(resp => {
      console.log(resp.data);
      var cedula = document.getElementById("cedulaEliminar");
      var nombre = document.getElementById("nombreEliminar");
      var apellido = document.getElementById("apellidoEliminar");
      var fecha = document.getElementById("fechaEliminar");
      var correo = document.getElementById("correoEliminar");
      var celular = document.getElementById("celularEliminar");
      cedula.value = resp.data.cc;
      nombre.value = resp.data.nombre1
      apellido.value = resp.data.apellido1
      fecha.value = resp.data.fecha
      correo.value = resp.data.correo
      celular.value = resp.data.celular
    });
}


function limpiarCamposEliminar() {
  var cedula = document.getElementById("cedulaEliminar");
  var nombre = document.getElementById("nombreEliminar");
  var apellido = document.getElementById("apellidoEliminar");
  var fecha = document.getElementById("fechaEliminar");
  var correo = document.getElementById("correoEliminar");
  var celular = document.getElementById("celularEliminar");
  cedula.value = ""
  nombre.value = ""
  apellido.value = ""
  fecha.value = ""
  correo.value = ""
  celular.value = ""
}

function eliminarPersona() {
  cedula = document.getElementsByName("cedulafiltrar2")[0].value;
  axios.delete("http://127.0.0.1:8000/persona/eliminar/" + cedula + "/", {
  })
    .then(function (response) {
      console.log(response);
      limpiarCamposEliminar();
    })
    .catch(function (error) {
      console.log(error);
    });
}