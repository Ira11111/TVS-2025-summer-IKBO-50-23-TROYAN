const VotingSystem = require('../voting_system');

describe('VotingSystem - SDD Tests', () => {
    let votingSystem;

    beforeEach(() => {
        votingSystem = new VotingSystem();
    });

    // Табличные тесты на основе спецификаций
    const testCases = [
        {
            description: 'Простое голосование с одним кандидатом',
            votingId: 'simple_vote',
            candidates: ['Option A'],
            votes: [
                { voter: 'v1', candidate: 'Option A' }
            ],
            expectedResults: { 'Option A': 1 },
            expectedTotal: 1
        },
        {
            description: 'Голосование с тремя кандидатами и равным распределением',
            votingId: 'three_way',
            candidates: ['Red', 'Green', 'Blue'],
            votes: [
                { voter: 'v1', candidate: 'Red' },
                { voter: 'v2', candidate: 'Green' },
                { voter: 'v3', candidate: 'Blue' }
            ],
            expectedResults: { 'Red': 1, 'Green': 1, 'Blue': 1 },
            expectedTotal: 3
        },
        {
            description: 'Голосование с явным лидером',
            votingId: 'leader_election',
            candidates: ['Alice', 'Bob', 'Charlie'],
            votes: [
                { voter: 'v1', candidate: 'Alice' },
                { voter: 'v2', candidate: 'Alice' },
                { voter: 'v3', candidate: 'Alice' },
                { voter: 'v4', candidate: 'Bob' },
                { voter: 'v5', candidate: 'Charlie' }
            ],
            expectedResults: { 'Alice': 3, 'Bob': 1, 'Charlie': 1 },
            expectedTotal: 5
        },
        {
            description: 'Голосование без голосов',
            votingId: 'no_votes',
            candidates: ['Candidate 1', 'Candidate 2'],
            votes: [],
            expectedResults: { 'Candidate 1': 0, 'Candidate 2': 0 },
            expectedTotal: 0
        }
    ];

    testCases.forEach((testCase, index) => {
        test(`SDD Test ${index + 1}: ${testCase.description}`, () => {
            // Создание голосования
            votingSystem.createVoting(testCase.votingId, testCase.candidates);
            
            // Регистрация голосов
            testCase.votes.forEach(vote => {
                votingSystem.registerVote(testCase.votingId, vote.voter, vote.candidate);
            });
            
            // Проверка результатов
            const results = votingSystem.countVotes(testCase.votingId);
            
            expect(results.votingId).toBe(testCase.votingId);
            expect(results.results).toEqual(testCase.expectedResults);
            expect(results.totalVotes).toBe(testCase.expectedTotal);
        });
    });

    describe('Тесты граничных условий', () => {
        test('Обработка большого количества голосов', () => {
            const votingId = 'mass_voting';
            const candidates = ['Yes', 'No'];
            
            votingSystem.createVoting(votingId, candidates);
            
            // Симуляция 1000 голосов
            for (let i = 0; i < 1000; i++) {
                const candidate = i % 3 === 0 ? 'No' : 'Yes'; // 2/3 за Yes, 1/3 за No
                votingSystem.registerVote(votingId, `voter${i}`, candidate);
            }
            
            const results = votingSystem.countVotes(votingId);
            
            expect(results.totalVotes).toBe(1000);
            // Примерное распределение (может немного отличаться из-за округления)
            expect(results.results.Yes).toBeGreaterThan(650);
            expect(results.results.No).toBeLessThan(350);
        });

        test('Голосование с одним участником', () => {
            votingSystem.createVoting('single_voter', ['Option 1', 'Option 2']);
            votingSystem.registerVote('single_voter', 'only_voter', 'Option 1');
            
            const results = votingSystem.countVotes('single_voter');
            
            expect(results.totalVotes).toBe(1);
            expect(results.results['Option 1']).toBe(1);
            expect(results.results['Option 2']).toBe(0);
        });
    });
});