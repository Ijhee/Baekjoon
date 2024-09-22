-- 코드를 입력하세요
SELECT 
    history_id as HISTROY_ID,
    car_id as CAR_ID,
    date_format(start_date, '%Y-%m-%d') as START_DATE,
    date_format(end_date, '%Y-%m-%d') as END_DATE,
    case when DATEDIFF(END_DATE,START_DATE)>= 29 then '장기 대여'
        else '단기 대여'
        end 
    as RENT_TYPE 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY 
where START_DATE between '2022-09-01' and '2022-09-30'
order by history_id desc