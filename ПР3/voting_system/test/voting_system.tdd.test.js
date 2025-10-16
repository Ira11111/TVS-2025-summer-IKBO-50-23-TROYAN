const VotingSystem = require('../voting_system');

describe('VotingSystem - TDD Tests', () => {
    let votingSystem;

    beforeEach(() => {
        votingSystem = new VotingSystem();
    });

    describe('Создание голосования', () => {
        test('должно создавать голосование с указанными кандидатами', () => {
            const voting = votingSystem.createVoting('election1', ['Alice', 'Bob', 'Charlie']);
            
            expect(voting.id).toBe('election1');
            expect(voting.candidates.has('Alice')).toBe(true);
            expect(voting.candidates.has('Bob')).toBe(true);
            expect(voting.candidates.has('Charlie')).toBe(true);
            expect(voting.isActive).toBe(true);
        });

        test('должно выбрасывать ошибку при создании голосования с существующим ID', () => {
            votingSystem.createVoting('election1', ['Alice', 'Bob']);
            
            expect(() => {
                votingSystem.createVoting('election1', ['Charlie', 'David']);
            }).toThrow('Голосование с ID election1 уже существует');
        });
    });

    describe('Регистрация голосов', () => {
        beforeEach(() => {
            votingSystem.createVoting('election1', ['Alice', 'Bob']);
        });

        test('должно успешно регистрировать голос', () => {
            const result = votingSystem.registerVote('election1', 'voter1', 'Alice');
            
            expect(result).toBe(true);
            
            const voting = votingSystem.getVotingStatus('election1');
            expect(voting.candidates.get('Alice')).toBe(1);
            expect(voting.voters.has('voter1')).toBe(true);
        });

        test('должно выбрасывать ошибку при повторном голосовании', () => {
            votingSystem.registerVote('election1', 'voter1', 'Alice');
            
            expect(() => {
                votingSystem.registerVote('election1', 'voter1', 'Bob');
            }).toThrow('Голосующий уже проголосовал');
        });

        test('должно выбрасывать ошибку при голосовании за несуществующего кандидата', () => {
            expect(() => {
                votingSystem.registerVote('election1', 'voter1', 'Eve');
            }).toThrow('Кандидат Eve не существует');
        });

        test('должно выбрасывать ошибку при голосовании в несуществующем голосовании', () => {
            expect(() => {
                votingSystem.registerVote('nonexistent', 'voter1', 'Alice');
            }).toThrow('Голосование с ID nonexistent не найдено');
        });
    });

    describe('Подсчет голосов', () => {
        test('должен корректно подсчитывать голоса', () => {
            votingSystem.createVoting('election1', ['Alice', 'Bob']);
            
            votingSystem.registerVote('election1', 'voter1', 'Alice');
            votingSystem.registerVote('election1', 'voter2', 'Bob');
            votingSystem.registerVote('election1', 'voter3', 'Alice');
            
            const results = votingSystem.countVotes('election1');
            
            expect(results.results.Alice).toBe(2);
            expect(results.results.Bob).toBe(1);
            expect(results.totalVotes).toBe(3);
        });

        test('должен возвращать нулевые результаты для новых голосований', () => {
            votingSystem.createVoting('election1', ['Alice', 'Bob']);
            
            const results = votingSystem.countVotes('election1');
            
            expect(results.results.Alice).toBe(0);
            expect(results.results.Bob).toBe(0);
            expect(results.totalVotes).toBe(0);
        });
    });

    describe('Завершение голосования', () => {
        test('должно завершать голосование и запрещать новые голоса', () => {
            votingSystem.createVoting('election1', ['Alice', 'Bob']);
            
            votingSystem.endVoting('election1');
            
            const voting = votingSystem.getVotingStatus('election1');
            expect(voting.isActive).toBe(false);
            
            expect(() => {
                votingSystem.registerVote('election1', 'voter1', 'Alice');
            }).toThrow('Голосование завершено');
        });
    });
});