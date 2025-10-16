class VotingSystem {
    constructor() {
        this.votings = new Map();
        this.voters = new Set();
    }

    createVoting(votingId, candidates) {
        if (this.votings.has(votingId)) {
            throw new Error(`Голосование с ID ${votingId} уже существует`);
        }

        const voting = {
            id: votingId,
            candidates: new Map(candidates.map(candidate => [candidate, 0])),
            isActive: true,
            voters: new Set()
        };

        this.votings.set(votingId, voting);
        return voting;
    }

    registerVote(votingId, voterId, candidate) {
        if (!this.votings.has(votingId)) {
            throw new Error(`Голосование с ID ${votingId} не найдено`);
        }

        const voting = this.votings.get(votingId);

        if (!voting.isActive) {
            throw new Error('Голосование завершено');
        }

        if (voting.voters.has(voterId)) {
            throw new Error('Голосующий уже проголосовал');
        }

        if (!voting.candidates.has(candidate)) {
            throw new Error(`Кандидат ${candidate} не существует`);
        }

        // Регистрируем голос
        voting.candidates.set(candidate, voting.candidates.get(candidate) + 1);
        voting.voters.add(voterId);
        this.voters.add(voterId);

        return true;
    }

    countVotes(votingId) {
        if (!this.votings.has(votingId)) {
            throw new Error(`Голосование с ID ${votingId} не найдено`);
        }

        const voting = this.votings.get(votingId);
        const results = {};

        for (const [candidate, votes] of voting.candidates) {
            results[candidate] = votes;
        }

        return {
            votingId: votingId,
            results: results,
            totalVotes: voting.voters.size,
            isActive: voting.isActive
        };
    }

    displayResults(votingId) {
        const results = this.countVotes(votingId);
        
        console.log(`\n=== Результаты голосования ${votingId} ===`);
        console.log(`Всего голосов: ${results.totalVotes}`);
        console.log('Результаты по кандидатам:');
        
        for (const [candidate, votes] of Object.entries(results.results)) {
            console.log(`  ${candidate}: ${votes} голосов`);
        }
        
        return results;
    }

    endVoting(votingId) {
        if (!this.votings.has(votingId)) {
            throw new Error(`Голосование с ID ${votingId} не найдено`);
        }

        this.votings.get(votingId).isActive = false;
        return true;
    }

    getVotingStatus(votingId) {
        if (!this.votings.has(votingId)) {
            throw new Error(`Голосование с ID ${votingId} не найдено`);
        }

        return this.votings.get(votingId);
    }
}

module.exports = VotingSystem;