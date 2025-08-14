with 
Total_mcap as (
                 select *,
                  sum(market_cap) over(partition by sector) as Total_Mcap_sector 
				  from stock_base),
Weightage_return as (select *,market_cap/Total_Mcap_sector as Weightage from Total_mcap),

performance as ( select *,Weightage*percentage as Today_performance from Weightage_return),

Expensive_stock as(
select* ,rank() over (partition by sector order by market_cap DESC) AS Expensive from performance)

select * from Expensive_stock
where Expensive<6


