# 🥬 TP — Redis : Cache des fiches plantes

## 🎯 Objectif

Mettre en cache les réponses de l’API `/api/plantes/:nom` dans Redis afin de :

- ⚡ Améliorer la vitesse de réponse utilisateur
- 💾 Réduire les appels inutiles au backend ou à la base de données
- 🧠 Appliquer le pattern **cache-aside**

---

## 🔧 Setup

### 1. Démarrer Redis avec Docker

```bash
docker run --name soclose-redis -p 6379:6379 -d redis
```

### 2. Initialiser un projet Node.js

```bash
npm init -y
npm install express ioredis
```

---

## 🧪 Code minimal

### `index.js`

```js
const express = require("express");
const Redis = require("ioredis");
const app = express();
const redis = new Redis();

const fakeDb = {
  "menthe": { nom: "Menthe", arrosage: "modéré", ensoleillement: "mi-ombre", saison: "été" },
  "tomate": { nom: "Tomate", arrosage: "fréquent", ensoleillement: "plein soleil", saison: "été" }
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
  console.log("🌱 API So-Close sur http://localhost:3000");
});
```

---

## 🔍 À faire

### Visualiser les clés dans Redis CLI

```bash
docker exec -it soclose-redis redis-cli
> KEYS plante:*
> GET plante:menthe
> TTL plante:menthe
```

---

## 💡 Concepts introduits

| Concept              | Description                                                  |
|----------------------|--------------------------------------------------------------|
| Cache-aside pattern  | Lecture du cache avant fallback vers la DB                   |
| TTL (Time To Live)   | Expiration automatique des données en cache (`EX 3600`)      |
| Prefixing des clés   | Organisation des entrées Redis (`plante:<nom>`)              |
| Gain de performance  | Temps de réponse réduit grâce au cache Redis                 |

---

## 🛠️ Bonus

- Ajouter un middleware pour chronométrer le temps de réponse
- Créer un endpoint `/admin/cache/:nom` pour supprimer une seule entrée
- Simuler une latence avec `setTimeout` dans `getPlanteFromDb()`
