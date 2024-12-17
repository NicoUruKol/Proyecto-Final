const productos = [
    {
        codigo: 900001, 
        bodega: "Combo",
        cepa: "Blend",
        imagen: "./imagenes/duoCaroGarzon.jpg",
        nombre: "Duo Caro Balasto",
        anio: 2024,
        precio: 345800,
        precioConDesc: 294780,  
        precioCuota: 98260,
        }, 
    {
        codigo: 900002,
        bodega: "Combo",
        cepa: "Blend",
        imagen: "./imagenes/GarzonCopas.jpg",
        nombre: "Dou Single Vineyard",
        anio: 2024,
        precio: 91600,
        precioConDesc: 77860,
        precioCuota: 25954,
        },
    {
        codigo: 900003,
        bodega: "Combo",
        cepa: "Blend",
        imagen: "./imagenes/GrazonBlanco.jpg",
        nombre: "Trio De Blancos",
        anio: 2024,
        precio: 52800,
        precioConDesc: 44880,
        precioCuota: 14960,
        }
    ]

/*console.log(productos);*/


let combosPromo = "";
for(let indice = 0; indice < productos.length; indice++){
    combosPromo +=`
                <div class="card-promo">
                    <a href="">
                        <img src=${productos[indice].imagen}
                    </a>
                    <h3>${productos[indice].nombre}</h3>
                    <p><del>$ ${productos[indice].precio.toLocaleString('de-DE')}</del>   ♦  <strong>$ ${productos[indice].precioConDesc.toLocaleString('de-DE')}</strong></p>
                    <p><b>3</b> <small>cuotas sin interes de </small><b>$ ${productos[indice].precioCuota.toLocaleString('de-DE')}</b></p>
                    <div class="card-promo-miniatura">
                        <a href="#">
                            <img title="Agregar al carrito" src="imagenes/cart-plus-solid.svg" alt="Imagen predeterminada" class="cambio-imagen">
                        </a>
                    </div>
                </div>
                `;
    }

const contenedorCursos = document.getElementById("combosContenedor");
contenedorCursos.innerHTML = combosPromo



function abrirModal(src) {
    document.getElementById("modalImagen").style.display = "block";
    document.getElementById("imagenAmpliada").src = src;
    }

function cerrarModal() {
    document.getElementById("modalImagen").style.display = "none";
    }
