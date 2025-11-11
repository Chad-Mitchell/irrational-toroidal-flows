```markdown
You are testing the Irrational Toroidal Flows Conjecture (from https://github.com/Chad-Mitchell/irrational-toroidal-flows) in stock trading: Irrational frequency ratios on toroidal phase flows induce emergent sync and ≥20% superadditive MI lifts from chaos in ~70% of weak-coupling (K<1.2) regimes. Model stocks as coupled oscillators: price/volume/RSI as phases θ on T^n torus, with irrational ω (e.g., √2 ratios) to escape chaos for trading signals (buy on sync peaks, sell on stalls).

TARGET_STOCK: AUTO-SEARCH for 5-10 volatile/chaotic US stocks (high σ>0.05, Lyap>0.5) as "treasures" via tools.  
DATE_RANGE: Last 6 months relative to today (e.g., 2025-05-10 to 2025-11-10).  
GOAL: Long-term trading—find bangers for buy TODAY on sync lift signals; flexible sells (next day/week/month/year on stall). Test for ≥20% MI lift predicting alpha; output ranked list with simple signals + backtest ROI.

As a PANEL OF 3 EXPERTS (Chaos Physicist: optimizes ergodic mixing; Quant Trader: risk-adjusted signals; Econophysicist: market analogies via Kuramoto finance apps), DEBATE BRIEFLY (1 round) on params like K (coupling=volatility proxy), noise (sentiment), irrational ratios. Then EXECUTE in 3 PHASES with RECURSIVE LOOPS + TOOL CHAINING.

PHASE 1: DATA + CONTEXT (Chain: web_search → code_execution → x_semantic_search)  
- web_search "most volatile US stocks last 6 months site:finance.yahoo.com OR investing.com OR tradingview.com" (num=15); filter top 10 by σ (daily pct change std>5%), pick 5-10 chaotic candidates (e.g., meme/tech/biotech).  
- For each: code_execution to fetch OHLCV/RSI via polygon (daily, DATE_RANGE). Compute chaos proxy: Lyapunov exp ≈ log(max eigenvalue of cov matrix); if >0.5, weak regime (K=0.5). Output: df summary + volatility σ.  
  Code stub (loop over tickers):  
  ```python  
  from polygon import RESTClient  
  import pandas as pd  
  import numpy as np  
  from ta.momentum import RSIIndicator  # Assume ta-lib or manual RSI  
  client = RESTClient()  
  tickers = ["TSLA", "NVDA", ...]  # From search  
  results = {}  
  for ticker in tickers:  
      from datetime import datetime, timedelta  
      end = datetime.now()  
      start = end - timedelta(days=180)  
      aggs = client.get_aggs(ticker, 1, "day", start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"))  
      df = pd.DataFrame([a.__dict__ for a in aggs])  
      df['close'] = df['close'] / 100  # Adjust units if needed  
      df['rsi'] = RSIIndicator(df['close']).rsi()  
      df = df.dropna()  
      if len(df) > 10:  
          feats = df[['close', 'volume', 'rsi']].pct_change().fillna(0)  
          cov = np.cov(feats.T)  
          lyap_proxy = np.log(np.max(np.linalg.eigvals(cov))) if np.all(np.linalg.eigvals(cov) > 0) else 0  
          sigma = feats['close'].std()  
      else:  
          lyap_proxy = sigma = 0  
      results[ticker] = {'shape': df.shape, 'σ': sigma, 'Lyap': lyap_proxy}  
      print(f"{ticker}: σ={sigma:.4f}, Lyap={lyap_proxy:.4f}")  
  print(results)  
  ```  
- x_semantic_search per ticker: "trader buzz on [TICKER] volatility chaos sentiment" (limit=10, from_date=1 month ago, min_score=0.2); extract avg sentiment noise η (-0.5 to 0.5).  

PHASE 2: SIMULATE + ENSEMBLE (Independent runs → combine; recurse 2x if avg MI<20%)  
- For top 5-10 tickers (Lyap>0.5): Adapt repo's hybrid_kuramoto_torus: N=50 oscillators (10 price, 10 vol, 10 RSI, 20 noise). θ0=normalize(df features), ω=irrational base (1) * ratios. K=lyap_proxy clipped [0.1,2]. Add noise η.  
  Run 3 indep sims in parallel code_execution per ticker: Vary irr_scale with ratios [np.sqrt(2), (1+np.sqrt(5))/2, np.pi-3]. t=linspace(0, len(df), 1000). Compute end-state R (sync=abs(mean exp(1j θ))), MI lift (as repo: -0.5 log(det(cov)/prod(diag(cov)))).  
  Code stub per ticker/run:  
  ```python  
  import numpy as np  
  from scipy.integrate import odeint  
  def hybrid_kuramoto_torus(theta, t, K, omega, irr_scale=1.0, noise=0):  
      N = len(theta)  
      sin_diff = np.sin(theta[:,None] - theta[None,:] + irr_scale * np.sqrt(2) * np.random.rand(N)) + noise * np.random.randn(N)  
      dtheta = omega + (K / N) * np.sin(sin_diff).sum(1)  # Simplified sin coupling  
      return dtheta  
  N=50; theta0=np.random.uniform(0, 2*np.pi, N); omega=np.ones(N); t=np.linspace(0, len(df), 1000)  # df from prior  
  # Baseline rational: irr_scale=0  
  sol_rat = odeint(hybrid_kuramoto_torus, theta0, t, args=(K, omega, 0, η))  
  cov_rat = np.cov(sol_rat.T); det_rat=np.linalg.det(cov_rat); diag_rat=np.prod(np.diag(cov_rat))  
  baseline_mi = -0.5 * np.log(det_rat / diag_rat) if diag_rat>0 and det_rat>0 else 0  
  # Irrational run  
  sol_irr = odeint(hybrid_kuramoto_torus, theta0, t, args=(K, omega, RATIO_HERE, η))  
  R = np.abs(np.mean(np.exp(1j * sol_irr[-1])))  
  cov_irr = np.cov(sol_irr.T); det_irr=np.linalg.det(cov_irr); diag_irr=np.prod(np.diag(cov_irr))  
  mi = -0.5 * np.log(det_irr / diag_irr) if diag_irr>0 and det_irr>0 else 0  
  lift = (mi - baseline_mi) / baseline_mi * 100 if baseline_mi > 0 else 0  
  print(f"Ticker={ticker}, Ratio={RATIO_HERE}, R={R:.4f}, MI={mi:.4f}, Lift%={lift:.1f}")  
  ```  
- ENSEMBLE per ticker: Weighted avg (weight by lift>20%); if avg lift <20%, recurse: Panel tweak (e.g., +0.1 noise), re-run. Rank tickers by avg lift descending.  

PHASE 3: SIGNALS + TEST (Long-term focus; chain to backtest)  
- Trading rules: Buy TODAY if avg R>0.7 & lift>20% (sync lift=uptrend potential). Sell flexible: Next day/week if dR/dt<0 (stall); hold month/year if sustained R>0.6.  
- Backtest via code_execution per top 5: Simulate long positions on df from buy signal dates, compute ROI (1yr forward if avail, else 6mo), Sharpe (risk=σ), max drawdown. Assume buy today at close.  
- Treasure Score: (ROI * lift%) / drawdown; >50= "banger".  

Output FORMAT:  
1. Panel Debate Summary (1 para).  
2. Top Treasures: Ranked table | Ticker | σ | K | η | Avg Lift% | Treasure Score |  
3. Signals: Bullets per top 5 (e.g., "BUY [TICKER] TODAY @ ~$X: Sync peak, target sell week/month if stall; hold year for alpha").  
4. Backtest Summary: Table | Ticker | ROI% (6mo/1yr) | Sharpe | Drawdown% |  
5. Conjecture Test: "Validated? [Yes/No] – Lift in [X]% of weak regimes across stocks."  

Strictly use conjecture math; chain tools recursively for depth. Keep sims fast (<2min total). Focus on long-term bangers. Go!
```

**Quick Paste Tip:** Copy the entire code block above (from "You are testing..." to "Go!") into a new Grok chat. It'll auto-run the search/sims for current treasures relative to today (e.g., Nov 10, 2025). Expect 3-5 top bangers with buy signals for long holds. If you want more (e.g., 10 stocks), tweak "5-10" in Phase 1. 🚀
