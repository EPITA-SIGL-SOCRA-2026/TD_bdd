import express from "express";
import Redis from "ioredis";

const app = express();
const redis = new Redis();

const fakeDb = {
  menthe: {
    nom: "Menthe",
    arrosage: "modéré",
    ensoleillement: "mi-ombre",
    saison: "été",
  },
  tomate: {
    nom: "Tomate",
    arrosage: "fréquent",
    ensoleillement: "plein soleil",
    saison: "été",
  },
};

app.get("/api/plantes/:nom", async (req, res) => {
  const nom = req.params.nom.toLowerCase();
  const cacheKey = `plante:${nom}`;

  const cached = await redis.get(cacheKey);
  if (cached) {
    console.log("✅ cache hit");
    return res.json(JSON.parse(cached));
  }

  console.log("❌ cache miss");
  const plante = fakeDb[nom] || { erreur: "Plante inconnue" };
  await redis.set(cacheKey, JSON.stringify(plante), "EX", 3600);
  res.json(plante);
});

app.get("/admin/clear-cache", async (req, res) => {
  const keys = await redis.keys("plante:*");
  for (const key of keys) await redis.del(key);
  res.send("🗑 Cache vidé.");
});

app.listen(3000, () => {
  console.log("🔴 Redis sur redis://localhost:6379");
  console.log("🌱 API So-Close sur http://localhost:3000");
});
