const VotingSystem = require('../voting_system');

describe('VotingSystem - ATDD Tests', () => {
    let votingSystem;

    beforeEach(() => {
        votingSystem = new VotingSystem();
    });

    describe('Приёмочные тесты для сценариев голосования', () => {
        test('Каждый голос должен учитываться один раз', () => {
            // Настройка
            votingSystem.createVoting('president2024', ['Candidate A', 'Candidate B', 'Candidate C']);
            
            // Действие
            votingSystem.registerVote('president2024', 'voter001', 'Candidate A');
            votingSystem.registerVote('president2024', 'voter002', 'Candidate B');
            votingSystem.registerVote('president2024', 'voter003', 'Candidate A');
            
            // Проверка
            const results = votingSystem.countVotes('president2024');
            
            expect(results.totalVotes).toBe(3);
            expect(results.results['Candidate A']).toBe(2);
            expect(results.results['Candidate B']).toBe(1);
            expect(results.results['Candidate C']).toBe(0);
        });

        test('Голосующий не может проголосовать дважды', () => {
            votingSystem.createVoting('referendum', ['Yes', 'No']);
            
            votingSystem.registerVote('referendum', 'voter123', 'Yes');
            
            // Попытка повторного голосования
            expect(() => {
                votingSystem.registerVote('referendum', 'voter123', 'No');
            }).toThrow('Голосующий уже проголосовал');
            
            const results = votingSystem.countVotes('referendum');
            expect(results.totalVotes).toBe(1);
            expect(results.results.Yes).toBe(1);
            expect(results.results.No).toBe(0);
        });

        test('Голосование должно корректно завершаться и подсчитывать итоги', () => {
            votingSystem.createVoting('board_election', ['John', 'Jane', 'Mike']);
            
            // Регистрация голосов
            const voters = ['v1', 'v2', 'v3', 'v4', 'v5'];
            const votes = ['John', 'Jane', 'John', 'Mike', 'Jane'];
            
            voters.forEach((voter, index) => {
                votingSystem.registerVote('board_election', voter, votes[index]);
            });
            
            // Завершение голосования
            votingSystem.endVoting('board_election');
            
            // Проверка результатов
            const results = votingSystem.countVotes('board_election');
            
            expect(results.isActive).toBe(false);
            expect(results.totalVotes).toBe(5);
            expect(results.results.John).toBe(2);
            expect(results.results.Jane).toBe(2);
            expect(results.results.Mike).toBe(1);
        });

        test('Система должна обрабатывать несколько независимых голосований', () => {
            // Создание нескольких голосований
            votingSystem.createVoting('election1', ['A', 'B']);
            votingSystem.createVoting('election2', ['X', 'Y', 'Z']);
            
            // Голосование в первом
            votingSystem.registerVote('election1', 'voter1', 'A');
            votingSystem.registerVote('election1', 'voter2', 'B');
            
            // Голосование во втором
            votingSystem.registerVote('election2', 'voter1', 'X');
            votingSystem.registerVote('election2', 'voter2', 'Y');
            votingSystem.registerVote('election2', 'voter3', 'X');
            
            // Проверка независимости результатов
            const results1 = votingSystem.countVotes('election1');
            const results2 = votingSystem.countVotes('election2');
            
            expect(results1.totalVotes).toBe(2);
            expect(results1.results.A).toBe(1);
            expect(results1.results.B).toBe(1);
            
            expect(results2.totalVotes).toBe(3);
            expect(results2.results.X).toBe(2);
            expect(results2.results.Y).toBe(1);
            expect(results2.results.Z).toBe(0);
        });
    });
});