# Steam & Twitch Market Saturation, Reviews, and Competitive Dynamics
## Executive Summary
This project examines the relationship between Steam game market saturation, user review sentiment, and Twitch engagement to assess competitiveness across genres and individual titles. By integrating review volume, positive versus negative sentiment, release timing, and watch/play time metrics, the analysis highlights which games achieve sustained success versus those driven by short-term trends. The findings show that strong review performance does not always translate into high viewer engagement, revealing a disconnect between player adoption and audience interest. Overall, the project provides a holistic, data-driven perspective on how consumer sentiment, market competition, and streaming behavior interact within the PC gaming ecosystem.

## Tools Used
- Python 
- Power BI
- Excel

## Data Model
<p align="center">
  <img src="images/Screenshot 2026-01-14 180522.png" width="45%" />
  <img src="images/Screenshot 2026-01-14 180605.png" width="45%" />
</p>

<p align="center">
  <img src="images/Screenshot 2026-01-14 180545.png" width="45%" />
  <img src="images/Screenshot 2026-01-14 180626.png" width="45%" />
</p>

## Dashboard Pages
<p align="center">
  <img src="images/stp1.png" width="45%" />
  <img src="images/stp2.png" width="45%" />
</p>

<p align="center">
  <img src="images/stp3.png" width="45%" />
  <img src="images/stp4.png" width="45%" />
</p>

<p align="center">
  <img src="images/stp5.png" width="45%" />
  <img src="images/stp6.png" width="45%" />
</p>


## Key Insights
**Market Saturation Does Not Guarantee Engagement**
- Action and Indie genres dominate total review volume on Steam, indicating heavy market saturation, but this does not consistently translate into high Twitch watch time. Several highly reviewed games show relatively low viewer engagement, suggesting that player adoption and spectator interest follow different dynamics.

**A Small Number of Titles Drive Disproportionate Attention**
- Across both reviews and watch time, a small subset of games (e.g., Counter-Strike 2, major live-service titles) account for a large share of total engagement. This “winner-take-most” pattern highlights a highly competitive environment where new releases must compete not just within their genre, but against entrenched market leaders.
  - Some of these titles, such as Counter-Strike 2, have massive and well established e-sports scenes (competitive play).

**Review Sentiment Trends Scale with Release Volume**
- Genres experiencing rapid growth in the number of releases also show sharp increases in both positive and negative reviews over time. This indicates that higher production volume increases visibility and engagement, but also amplifies criticism, raising the reputational risk for developers entering saturated genres.

**Twitch Watch Time Favors Multiplayer and Replayable Games**
- Genres such as Action, Free-to-Play, and Massively Multiplayer generate substantially higher watch time relative to their release counts. This suggests that games with strong social, competitive, or replayable elements are more likely to sustain long-term viewer interest compared to single-session or narrative-focused titles.

**Trending Momentum Is Volatile and Short-Lived**
- Trending rankings show frequent position changes over short time windows, indicating that visibility spikes are often temporary. Games that maintain high rank over multiple weeks tend to have ongoing content updates or strong community engagement, reinforcing the importance of post-launch support.

**Watch Time and Play Time Are Related but Not Linear**
- While higher watch time generally aligns with increased play time, the relationship is uneven. Some games attract large audiences without equivalent play activity, implying they function more as spectator experiences, while others show strong player engagement but limited streaming appeal.

## Recommendations
**Prioritize Differentiation in Saturated Genres**
- Developers entering highly saturated genres such as Action or Indie should focus on clear mechanical, stylistic, or community-driven differentiation rather than competing on volume alone. High review density increases competition and visibility risk, making uniqueness a critical factor for discoverability.

**Use Review Sentiment as a Risk Indicator, Not Just a Score**
- Rising negative review volume in high-output genres suggests increased reputational risk. Monitoring review trends alongside release density can help developers anticipate backlash and prioritize polish, bug fixes, or scope control prior to launch.

**Treat Trending Status as a Short-Term Amplifier, Not a Guarantee**
- Trending visibility should be used as a launch and awareness accelerator rather than a long-term growth assumption.
- Planning for player retention is key, and teams need to strategize for post-launch support.
  - Implement content that drives community events.
  - Content updates need to be frequent.

## Limitations & Assumptions
- Genre categorization was non-trivial because games often have multiple genre tags, leading to multiple rows per game. As a result, genre-level analysis reflects tag presence rather than mutually exclusive genre classification.
- Some games contained corrupted or incomplete Steam records and were excluded from the Steam analysis. These titles still appear in Twitch data where available, which may cause minor discrepancies between platform comparisons.

## Conclusion
This project highlights the complexity of the PC gaming market by demonstrating that popularity, engagement, and competitiveness are influenced by multiple, interconnected factors rather than a single success metric. By analyzing Steam review data alongside Twitch watch and play time, the analysis shows that high market saturation increases competition without guaranteeing sustained visibility or engagement. The findings emphasize the importance of differentiating products, aligning engagement strategies with audience behavior, and planning beyond short-term trending momentum. Ultimately, this project reinforces how integrated, multi-source analysis can support more informed strategic decisions in highly competitive digital marketplaces.



