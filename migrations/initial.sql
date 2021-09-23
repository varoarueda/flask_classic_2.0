CREATE TABLE "movimientos"  (
	"id"	INTEGER,
	"fecha"	TEXT NOT NULL,
	"concepto"	TEXT NOT NULL,
	"ingreso_gasto"	TEXT NOT NULL,
	"cantidad"	REAL,
	PRIMARY KEY("id" AUTOINCREMENT)
)