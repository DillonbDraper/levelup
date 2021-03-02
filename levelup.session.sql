SELECT
                    e.id,
                    e.description,
                    e.date,
                    e.time,
                    g.title,
                    g.number_of_players,
                    g.skill_level,
                    gr.id,
                    u.id user_id,
                    u.first_name || ' ' || u.last_name AS full_name
                FROM
                    levelupapi_event e
                JOIN
                    levelupapi_game g ON e.game_id = g.id
                JOIN
                    levelupapi_gamer gr ON e.organizer_id = gr.id
                JOIN
                    auth_user u ON gr.user_id = u.id
                GROUP BY e.id