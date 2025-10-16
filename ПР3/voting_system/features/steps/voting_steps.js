const { Given, When, Then } = require('@cucumber/cucumber');
const { expect } = require('chai');
const VotingSystem = require('../../voting_system');

let votingSystem;
let currentVoting;
let errorMessage;

Given('голосование {string} запущено с кандидатами {string}', function (votingId, candidatesString) {
    votingSystem = new VotingSystem();
    const candidates = candidatesString.split(',').map(c => c.trim());
    currentVoting = votingSystem.createVoting(votingId, candidates);
});

When('участник {string} голосует за {string}', function (voterId, candidate) {
    try {
        votingSystem.registerVote(currentVoting.id, voterId, candidate);
    } catch (error) {
        errorMessage = error.message;
    }
});

Then('голос учитывается', function () {
    const results = votingSystem.countVotes(currentVoting.id);
    expect(results.totalVotes).to.be.greaterThan(0);
});

Then('участник {string} не может проголосовать повторно', function (voterId) {
    expect(errorMessage).to.include('уже проголосовал');
});

Then('отображаются результаты голосования', function () {
    const results = votingSystem.displayResults(currentVoting.id);
    expect(results).to.have.property('results');
    expect(results).to.have.property('totalVotes');
});

Then('{string} получает {int} голосов', function (candidate, expectedVotes) {
    const results = votingSystem.countVotes(currentVoting.id);
    expect(results.results[candidate]).to.equal(expectedVotes);
});