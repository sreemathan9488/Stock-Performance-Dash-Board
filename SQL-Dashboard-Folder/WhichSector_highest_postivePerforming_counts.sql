with 
Total_mcap as (
                 select *,
                  sum(market_cap) over(partition by sector) as Total_Mcap_sector 
				  from stock_base),
Weightage_return as (select *,market_cap/Total_Mcap_sector as Weightage from Total_mcap),

performance as ( select *,Weightage*percentage as Today_performance from Weightage_return)

select sector, count(price_diff) as performing_count from performance
where price_diff >0
group by sector 
order by performing_count DESC
limit 5
