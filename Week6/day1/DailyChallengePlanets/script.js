// const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];

// const listPlanets = document.querySelector('.listPlanets');

// const planetColors = ["gray", "orange", "blue", "red", "green", "gold", "lightblue", "violet"];

// planets.forEach((planetName, index) => {
//     const planetDiv = document.createElement("div");
//     planetDiv.className = "planet";
//     planetDiv.textContent = planetName;
//     planetDiv.style.backgroundColor = planetColors[index]; 
//     listPlanets.appendChild(planetDiv);
// });


// regarding the moon we should make an array of objects 

const planetsData = [
    {
        name: "Mercury",
        color: "gray",
        moons: 0,
    },
    {
        name: "Venus",
        color: "orange",
        moons: 0,
    },
    {
        name: "Earth",
        color: "blue",
        moons: 1,
    },
    {
        name: "Mars",
        color: "red",
        moons: 2,
    },
    {
        name: "Jupiter",
        color: "orange",
        moons: 79,
    },
    {
        name: "Saturn",
        color: "gold",
        moons: 83,
    },
    {
        name: "Uranus",
        color: "lightblue",
        moons: 27,
    },
    {
        name: "Neptune",
        color: "blue",
        moons: 14,
    },
];


const listPlanetsSection = document.querySelector(".listPlanets");

planetsData.forEach((planet) => {
    const planetDiv = document.createElement("div");
    planetDiv.className = "planet";
    planetDiv.style.backgroundColor = planet.color;
    planetDiv.textContent = planet.name;

    if (planet.moons > 0) {
        const moonParent = planetDiv;

        for (let i = 0; i < planet.moons; i++) {
            const moonDiv = document.createElement("div");
            moonDiv.className = "moon";
            moonParent.appendChild(moonDiv);
        }
    }

    listPlanetsSection.appendChild(planetDiv);
});