//Write a voting program as described below for small-scale meeting use. (8p)
// The program asks for the number of candidates.
// Then the program asks for the names of the candidates: Name for candidate 1
// Store the candidates names and initial vote count in objects like this:
function voting() {
    const candidatestr = prompt("How many candidates we have?");
    const candidates_count = parseInt(candidatestr);
    let candidates = []
    for (let i = 0; i < candidates_count; i++) {
        const name = prompt(`Type name of Candidate ${i + 1}:`);
        candidates.push({name: name, vote: 0});
    }
    const voters = prompt("How many voters we have?");
    const voters_count = parseInt(voters);
    for (let i = 0; i < voters_count; i++) {
        const vote = prompt(`Voter ${i + 1}, enter the name of the candidate you vote for (or press Enter for an empty vote):`);

        if (vote) {
            const candidate = candidates.find(c => c.name.toLowerCase() === vote.toLowerCase());
            if (candidate) {
                candidate.vote++;
            } else {
                console.log(`Candidate "${vote}" not found.`);
            }
        }
    }
    let winner = candidates [0]
    for (let i = 1; i < voters_count; i++) {
        if (candidates[i].vote > winner.vote) {
            winner = candidates[i]
        }
    }

    console.log(`The winner is ${winner.name} with ${winner.vote} votes.`);
    console.log("Results:");
    candidates.forEach(candidate => {
        console.log(`${candidate.name}: ${candidate.vote} votes`);
    });
}