#! /bin/env python

import MySQLdb

db = MySQLdb.connect("10.10.67.102","root","sd-9898w","db_gslb")
cursor = db.cursor()

def set_hostinfo():
    sql = "INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('A1CF7A69BF2BFA66436D648D2B63DA8F','auto.test.liubo.com','http','17006592',2,100,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('A1CF7A69BF2BFA66436D648D2B63DA8F','auto.test.liubo.com','http2','17039360',1,100,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('A1CF7A69BF2BFA66436D648D2B63DA8F','auto.test.liubo.com','https','17039616',3,101,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('A1CF7A69BF2BFA66436D648D2B63DA8F','auto.test.liubo.com','http3','17039872',2,101,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('A1CF7A69BF2BFA66436D648D2B63DA8F','auto.test.liubo.com','https','17040384',0,102,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('A1CF7A69BF2BFA66436D648D2B63DA8F','auto.test.liubo.com','https','17040640',0,103,100);"
    sql2 = "INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('D941F8E5C94BF38905D8525DB0446D6B','auto.test2.liubo.com','http','17006592',2,100,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('D941F8E5C94BF38905D8525DB0446D6B','auto.test2.liubo.com','http2','17039360',1,100,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('D941F8E5C94BF38905D8525DB0446D6B','auto.test2.liubo.com','https','17039616',3,101,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('D941F8E5C94BF38905D8525DB0446D6B','auto.test2.liubo.com','http3','17039872',2,101,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('D941F8E5C94BF38905D8525DB0446D6B','auto.test2.liubo.com','https','17040384',0,102,100);INSERT INTO host_info (host_id,host,protocol,ip,ip_weight,idc,load_limit)VALUES('D941F8E5C94BF38905D8525DB0446D6B','auto.test2.liubo.com','https','17040640',0,103,100);"
    insert_load1_info = "INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('6247E80F7AB09F55C2CF57B435D2154C', 'auto.load1.test.zhangxy.com', 'http', '17039616', '3', '1', '2');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('6247E80F7AB09F55C2CF57B435D2154C', 'auto.load1.test.zhangxy.com', 'https', '17039872', '2', '1', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('6247E80F7AB09F55C2CF57B435D2154C', 'auto.load1.test.zhangxy.com', 'http2', '16777728', '3', '2', '2');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('6247E80F7AB09F55C2CF57B435D2154C', 'auto.load1.test.zhangxy.com', 'http', '16778240', '4', '2', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('6247E80F7AB09F55C2CF57B435D2154C', 'auto.load1.test.zhangxy.com', 'https', '17040384', '1', '3', '100');"
    insert_differentIdc_info = "INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('77089547E43FF794C932F5F087B79BB2', 'auto.differentIdc.zhangxy.com', 'https', '17039616', '2', '1', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('77089547E43FF794C932F5F087B79BB2', 'auto.differentIdc.zhangxy.com', 'http', '16777728', '1', '2', '100');"
    insert_load2_info = "INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('C1C881C84DA8E068F1EE16559B6EB8B7', 'auto.load2.test.zhangxy.com', 'http', '17039616', '3', '1', '2', '0');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('C1C881C84DA8E068F1EE16559B6EB8B7', 'auto.load2.test.zhangxy.com', 'https', '17039872', '2', '1', '1', '0');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('C1C881C84DA8E068F1EE16559B6EB8B7', 'auto.load2.test.zhangxy.com', 'http', '16777728', '3', '2', '2', '0');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('C1C881C84DA8E068F1EE16559B6EB8B7', 'auto.load2.test.zhangxy.com', 'http', '16778240', '4', '2', '100', '0');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('C1C881C84DA8E068F1EE16559B6EB8B7', 'auto.load2.test.zhangxy.com', 'https', '17040384', '1', '3', '100', '0');"
    insert_load3_info = "INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('A30129E42AD8CC5C5AFC08C85CD4E503', 'auto.load3.test.zhangxy.com', 'http', '17039616', '3', '1', '2', '0');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('A30129E42AD8CC5C5AFC08C85CD4E503', 'auto.load3.test.zhangxy.com', 'https', '17039872', '2', '1', '6', '0');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('A30129E42AD8CC5C5AFC08C85CD4E503', 'auto.load3.test.zhangxy.com', 'https', '168435856', '1', '1', '5', '0');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('A30129E42AD8CC5C5AFC08C85CD4E503', 'auto.load3.test.zhangxy.com', 'http', '16777728', '3', '2', '2', '0');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('A30129E42AD8CC5C5AFC08C85CD4E503', 'auto.load3.test.zhangxy.com', 'http', '16778240', '4', '2', '100', '0');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('A30129E42AD8CC5C5AFC08C85CD4E503', 'auto.load3.test.zhangxy.com', 'https', '17040384', '1', '3', '100', '0');"
    
       
    insert_auto_test1 = "INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '17039616', '1', '1', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '16791552', '1', '2', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '16908800', '1', '3', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '16777728', '1', '4', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '17563648', '1', '5', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '1731993600', '1', '6', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '18413568', '1', '8', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '18415616', '1', '9', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '18417664', '1', '10', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '19005440', '1', '11', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '19136512', '1', '12', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '19202048', '1', '13', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '19398656', '1', '15', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '19660800', '1', '16', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '20165120', '1', '17', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '20165632', '1', '18', '100');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`) VALUES ('496E03919153088AD71D76BAD1D491C2', 'auto.test1.zhangxy.com', 'http', '20742144', '1', '19', '100', '0');"



    insert_auto_test2 = "INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`, `update_time`) VALUES ('3639FF7A5E9ACA146BD1BCCD2390044C', 'auto.test2.zhangxy.com', 'http', '1731993600', '1', '1', '100', '0', '2017-02-23 14:23:32');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`, `update_time`) VALUES ('3639FF7A5E9ACA146BD1BCCD2390044C', 'auto.test2.zhangxy.com', 'http', '1731996672', '1', '2', '100', '0', '2017-02-23 14:23:32');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`, `update_time`) VALUES ('3639FF7A5E9ACA146BD1BCCD2390044C', 'auto.test2.zhangxy.com', 'http', '18413568', '1', '3', '100', '0', '2017-02-23 14:23:32');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`, `update_time`) VALUES ('3639FF7A5E9ACA146BD1BCCD2390044C', 'auto.test2.zhangxy.com', 'http', '19202048', '1', '4', '100', '0', '2017-02-23 14:23:32');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`, `update_time`) VALUES ('3639FF7A5E9ACA146BD1BCCD2390044C', 'auto.test2.zhangxy.com', 'http', '19398656', '1', '5', '100', '0', '2017-02-23 14:23:32');INSERT INTO `db_gslb`.`host_info` (`host_id`, `host`, `protocol`, `ip`, `ip_weight`, `idc`, `load_limit`, `create_time`, `update_time`) VALUES ('3639FF7A5E9ACA146BD1BCCD2390044C', 'auto.test2.zhangxy.com', 'http', '20165120', '1', '6', '100', '0', '2017-02-23 14:23:32');"    



    cursor.execute(sql2)
        










    #cursor.execute(client_sql)



if __name__ == '__main__':
    pass
    #set_hostinfo()
    #set_ipdistribution()