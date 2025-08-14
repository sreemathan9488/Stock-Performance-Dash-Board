with 
Total_mcap as (
                 select *,
                  sum(market_cap) over(partition by sector) as Total_Mcap_sector 
				  from stock_base),
Weightage_return as (select *,market_cap/Total_Mcap_sector as Weightage from Total_mcap),

performance as ( select *,Weightage*percentage as Today_performance from Weightage_return),

Rank_data as(
             select *,

             rank() over (partition by sector order by today_price desc, today_performance desc) as Rank from performance)


select * from Rank_data
where Rank<4
and sector is not null and Today_performance>=0

