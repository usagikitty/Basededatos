from fastapi import FastAPI


from app.routers import jugador, jugador_inscripcion, participantes_jugadores, participantes_equipos, torneo, asociacion

app = FastAPI()


app.include_router(jugador.router)
app.include_router(jugador_inscripcion.router)
app.include_router(participantes_jugadores.router)
app.include_router(participantes_equipos.router)
app.include_router(torneo.router)
app.include_router(asociacion.router)