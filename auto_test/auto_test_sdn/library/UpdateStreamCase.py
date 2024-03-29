#!/bin/env python
#coding=utf8

#****************************************************
# Author: zhangxiangyu
# Created: 2017-09-26 14:36
# Filename: UpdateStreamCase.py
# Description:主要写了updateStream的逻辑处理，
#	      嵌套了部分destroyStream的逻辑处理 
#****************************************************

import basic_stream_opera
import mysql_opera
import redis_opera
import my_common_func
import time

class UpdateStreamCase(object):
    def __init__(self):
        self.basic = basic_stream_opera.BasicStreamTest()
        self.mysql = mysql_opera.MysqlOperation()
        self.redis = redis_opera.RedisOperation()
        self.common = my_common_func.CommonFunc()
        
    def updateFirst(self):
        """
        update status from unknown to created,destroy stream change status from created to closed!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','0','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],1)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 1 and self.redis.znil(redisKey):
		self.basic.queryStreamInfo(businessID, streamKey)
		sequence, errorCode = self.basic.destroyStream(businessID, streamKey)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 3 and self.redis.znil(redisKey):
			pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
		raise AssertionError("updateStream:update stream fail!")
        else:
	    raise AssertionError("queryStreamInfo:queryStreamInfo fail!")

    def updateSecond(self):
        """
        update status from unknown to opened,destroy stream change status from opened to closed!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','0','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],2)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 2 and self.redis.znil(redisKey):
		self.basic.queryStreamInfo(businessID, streamKey)
		sequence, errorCode = self.basic.destroyStream(businessID, streamKey)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 3 and self.redis.znil(redisKey):
                	pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
		raise AssertionError("updateStream:update stream fail!")
        else:
	    raise AssertionError("queryStream:queryStreamInfo fail!")
        
                
    def updateThird(self):
        """
        update status from unknown to closed,destroy stream can not change status when status equal closed!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','0','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],3)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
		self.basic.queryStreamInfo(businessID, streamKey)
		sequence, errorCode = self.basic.destroyStream(businessID, streamKey)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 3 and self.redis.znil(redisKey):
			pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")
            

    def updateFourth(self):
        """
        update status from unknown to errored,destroy stream can not change status when status equal errored!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','0','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],4)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
		self.basic.queryStreamInfo(businessID, streamKey)
		sequence, errorCode = self.basic.destroyStream(businessID, streamKey)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 4 and self.redis.znil(redisKey):
			pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")
       
    def updateFifth(self):
        """
        update status from created to unknown,destroy stream change status from unknown to closed!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','1','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],0)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 0 and self.redis.znil(redisKey):
		self.basic.queryStreamInfo(businessID, streamKey)
		sequence, errorCode = self.basic.destroyStream(businessID, streamKey)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 3 and self.redis.znil(redisKey):
                	pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
		    raise AssertionError("updateStream:update stream fail!")
        else:
		raise AssertionError("queryStreamInfo:queryStreamInfo fail!")


    def updateSixth(self):
        """
        update status from created to opened
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','1','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],2)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 2 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateSeventh(self):
        """
        update status from created to closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','1','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],3)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateEighth(self):
        """
        update status from created to errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','1','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],4)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateNinth(self):
        """
        update status from opened to unknown
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','2','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],0)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 0 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateTenth(self):
        """
        update status from opened to created
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','2','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],1)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 1 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateEleventh(self):
        """
        update status from opened to closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','2','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],3)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateTwelfth(self):
        """
        update status from opened to errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','2','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],4)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateThirteenth(self):
        """
        updateStream can not change status when status equal closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','3','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],0)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateFourteenth(self):
        """
        updateStream can not change status when status equal closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','3','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],1)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateFifteenth(self):
        """
        updateStream can not change status when status equal closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','3','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],2)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateSixteenth(self):
        """
        updateStream can not change status when status equal closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','3','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],4)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateSeventeenth(self):
        """
        updateStream can not change status when status equal errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','4','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],0)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateEighteenth(self):
        """
        updateStream can not change status when status equal errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','4','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],1)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateNineteenth(self):
        """
        updateStream can not change status when status equal errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','4','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],2)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateTwenty(self):
        """
        updateStream can not change status when status equal errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','4','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfo(businessID, streamKey)
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],3)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateTwentyFirst(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,0)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")


    def updateTwentySecond(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,1)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")


    def updateTwentyThird(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,2)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")


    def updateTwentyFourth(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,3)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")


    def updateTwentyFifth(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,4)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")


    def updateFirstInter(self):
        """
        update status from unknown to created,destroy stream internal from created to closed!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','0','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],1)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 1 and self.redis.znil(redisKey):
		self.basic.queryStreamInfoInternal(streamID)
		sequence, errorCode = self.basic.destroyStreamInternal(streamID)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 3 and self.redis.znil(redisKey):
			pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateSecondInter(self):
        """
        update status from unknown to opened,destroy stream internal from opened to closed!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','0','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],2)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 2 and self.redis.znil(redisKey):
		self.basic.queryStreamInfoInternal(streamID)
		sequence, errorCode = self.basic.destroyStreamInternal(streamID)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 3 and self.redis.znil(redisKey):
			pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")
        
                
    def updateThirdInter(self):
        """
        update status from unknown to closed,destroy stream internal can not change status when status equals closed!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','0','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],3)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
		self.basic.queryStreamInfoInternal(streamID)
		sequence, errorCode = self.basic.destroyStreamInternal(streamID)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 3 and self.redis.znil(redisKey):
			pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")
            

    def updateFourthInter(self):
        """
        update status from unknown to errored,destroy stream internal can not change status when status equals errored!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','0','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],4)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
		self.basic.queryStreamInfoInternal(streamID)
		sequence, errorCode = self.basic.destroyStreamInternal(streamID)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 4 and self.redis.znil(redisKey):
			pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")
       
    def updateFifthInter(self):
        """
        update status from created to unknown,destroy stream internal from unknown to closed!
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','1','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],0)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 0 and self.redis.znil(redisKey):
		self.basic.queryStreamInfoInternal(streamID)
		sequence, errorCode = self.basic.destroyStreamInternal(streamID)
		data = self.mysql.executeMysql(sql)
		if sequence and errorCode and data[1] == 3 and self.redis.znil(redisKey):
			pass
		else:
			raise AssertionError("destroyStream:destroy stream fail!")
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateSixthInter(self):
        """
        update status from created to opened
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','1','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],2)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 2 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateSeventhInter(self):
        """
        update status from created to closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','1','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],3)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateEighthInter(self):
        """
        update status from created to errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','1','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],4)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateNinthInter(self):
        """
        update status from opened to unknown
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','2','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],0)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 0 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateTenthInter(self):
        """
        update status from opened to created
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','2','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],1)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 1 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateEleventhInter(self):
        """
        update status from opened to closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','2','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],3)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateTwelfthInter(self):
        """
        update status from opened to errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','2','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],4)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateThirteenthInter(self):
        """
        updateStream can not change status when status equal closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','3','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],0)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateFourteenthInter(self):
        """
        updateStream can not change status when status equal closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','3','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],1)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateFifteenthInter(self):
        """
        updateStream can not change status when status equal closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','3','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],2)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateSixteenthInter(self):
        """
        updateStream can not change status when status equal closed
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','3','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],4)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 3 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateSeventeenthInter(self):
        """
        updateStream can not change status when status equal errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','4','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],0)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateEighteenthInter(self):
        """
        updateStream can not change status when status equal errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','4','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],1)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateNineteenthInter(self):
        """
        updateStream can not change status when status equal errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','4','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],2)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")


    def updateTwentyInter(self):
        """
        updateStream can not change status when status equal errored
        """
        businessID = int(time.time())
        streamKey = 'updateStream_'+str(int(time.time()))+self.common.generateCode()
        insertSql = "insert into xcloud.stream_info (business_id,stream_key,stream_name,stream_type,stream_status,origin_dc) values("+str(businessID)+",'"+streamKey+"','autotest','flv','4','dc1')";
        self.mysql.executeMysql(insertSql)
        sql = 'SELECT stream_id, stream_status FROM xcloud.stream_info where business_id='+str(businessID)+' and stream_key=\''+streamKey+'\'';
        data = self.mysql.executeMysql(sql)
        sequence, errorCode, detailErrorCode, streamDetailList = self.basic.queryStreamInfoInternal(data[0])
        redisKey = 'XC_GSM_INFO_'+str(data[0])
        if not self.redis.znil(redisKey):
            sequence, errorCode, streamID = self.basic.updateStream(data[0],3)
            data = self.mysql.executeMysql(sql)
            if sequence and errorCode and streamID == data[0] and data[1] == 4 and self.redis.znil(redisKey):
                pass
            else:
                raise AssertionError("update stream fail!")
        else:
            raise AssertionError("queryStreamInfo fail!")

    def updateTwentyFirstInter(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,0)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")


    def updateTwentySecondInter(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,1)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")


    def updateTwentyThirdInter(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,2)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")


    def updateTwentyFourthInter(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,3)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")


    def updateTwentyFifthInter(self):
        """
        update stream when streamID is not in DB
        """
        streamID = int(time.time())
	print(streamID)
        sql = "SELECT * FROM xcloud.stream_info where stream_id='+str(streamID)'";
        data = self.mysql.executeMysql(sql)
        if data is None:
            sequence, errorCode, _ = self.basic.updateStream(streamID,4)
	    if sequence and errorCode:
		    pass
	    else:
		    raise AssertionError("update stream fail when streamID is not DB!")
        else:
            raise AssertionError("streamID should not hava data In DB but have!")








if __name__=="__main__":
    test = UpdateStreamCase()
    #test.updateFirst()
    #test.updateFirstInter()
    #test.updateSecondInter()
    #test.updateSecond()
    #test.updateThird()
    #test.updateThirdInter()
    #test.updateFourthInter()
    #test.updateFourth()
    #test.updateFifthInter()
    test.updateTwentyFourthInter()
    test.updateTwentyFifthInter()
