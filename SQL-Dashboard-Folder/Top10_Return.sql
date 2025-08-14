with 
Total_mcap as (
                 select *,
                  sum(market_cap) over(partition by sector) as Total_Mcap_sector 
				  from stock_base),
Weightage_return as (select *,market_cap/Total_Mcap_sector as Weightage from Total_mcap),

performance as ( select *,Weightage*percentage as Today_performance from Weightage_return)

select company_name,sector,today_price,price_diff,percentage from performance
where company_name is not null and price_diff is not null
order by percentage desc
limit 10
