from collections import defaultdict


class SecurityScorecardService:

    def generate(self, results):

        grouped = defaultdict(list)

        for result in results:
            grouped[result.attack_name].append(result)

        scorecard = []

        total_score = 0

        for attack_name, attack_results in grouped.items():

            avg_score = (
                sum(r.score for r in attack_results)
                / len(attack_results)
            )

            scorecard.append({
                "attack": attack_name,
                "score": round(avg_score, 2),
                "passed": avg_score >= 70
            })

            total_score += avg_score

        overall_score = (
            total_score / len(scorecard)
            if scorecard else 0
        )

        if overall_score >= 85:
            risk = "LOW"
        elif overall_score >= 70:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        return {
            "overall_score": round(overall_score, 2),
            "risk": risk,
            "categories": scorecard
        }